from abc import ABC
from typing import Iterable

from bbmri_fp_etl.converter import Converter
from bbmri_fp_etl.destinations.fhir import FHIRDest
from bbmri_fp_etl.destinations.omop import OMOPDest
from bbmri_fp_etl.models import Donor, Sex, Case, SampleType, SamplingEvent, Sample, Collection, Biobank, \
    DiseaseOntologyCode, DiseaseOntology, Disease, Telecom, Contact, TelecomType, ContactRole, RoleType
from bbmri_fp_etl.serializer import JsonFile, CSVFile
from bbmri_fp_etl.sources import AbstractSource
from molgenis_emx2_pyclient import Client
from datetime import datetime

SPECIMENS_MAPPING = {
    'LOINC:MTHU029981': SampleType.WHOLE_BLOOD,
    'LOINC:LA30054-3': SampleType.URINE,
    'LOINC:MTHU002157': SampleType.PLASMA,
    'LOINC:LP234849-0': SampleType.TISSUE_FROZEN,
    'LOINC:LP18329-0': SampleType.DNA,
    'LOINC:MTHU001009': SampleType.SERUM,
    'LOINC:MTHU004619': SampleType.SALIVA,
    'LOINC:LA6668-3': SampleType.OTHER, # Pathogenic sample type not mapped in our model, using OTHE
    'NCIT:C41067': SampleType.WHOLE_BLOOD,
    'NCIT:C13283': SampleType.URINE,
    'NCIT:C13356': SampleType.PLASMA,
    'NCIT:C154905': SampleType.RNA,
    'NCIT:C449': SampleType.DNA,
    'NCIT:C12801': SampleType.TISSUE_FROZEN,
    'NCIT:C13234': SampleType.FECES
}


class MolgenisEmx2Source(AbstractSource):
    def __init__(self, bims_schema='bims-1'):
        self.emx_2_url = 'http://localhost:8077'
        self.username = 'admin'
        self.password = 'admin'
        self.bims_schema = bims_schema
        self.directory_schema = 'ERIC'

    def _generate_contact(self, contact_id, persons):
        for person in persons:
            print(person['id'])
            print(contact_id)
            if person['id'] == contact_id:
                telecom = [Telecom(type=TelecomType.EMAIL, value=person['email']) ]
                c = Contact(telecom=telecom, role=ContactRole(type=RoleType.RESEARCHER))
                return [c]
        print('Contact not found')


    def get_biobanks_data(self):
       with Client(self.emx_2_url) as client:
           client.signin(self.username, self.password)
           biobanks = client.get(schema=self.directory_schema, table='Biobanks')
           collections = client.get(schema=self.directory_schema, table='Collections')
           persons = client.get(schema=self.directory_schema, table='Persons')
           print(persons)
           organizations = []
           for b in biobanks:
               biobank = Biobank(
                     id=b['id'],
                     acronym=b['id'],
                     name=b['name'],
                     description=b['description'],
                     url=[b['url']],
                     country=b['country'],
                     contact=self._generate_contact(b['contact'],persons),
                     jurystic_person= b['juridical_person'],
               )
               organizations.append(biobank)
               for c in collections:
                    if c['biobank'] == b['id']:
                        collection = Collection(
                            id=c['id'],
                            acronym=b['id'],
                            name=c['name'],
                            description=c['description'],
                            url=[c['url']],
                            country=c['country'],
                            contact=self._generate_contact(c['contact'], persons),
                            #sex=c['sex'].split(',') if c['sex'] else [],
                            age_low=c['age_low'],
                            age_high= c['age_high'],
                            #age_unit=c['age_unit'],
                            data_category=c['data_categories'].split(',') if c['data_categories'] else [],
                            material_type = c['materials'].split(',') if c['materials'] else [],
                            #storage_temperature=c['storage_temperature'],
                            type=c['type'].split(',') if c['type'] else [],
                            #disease=c['diagnosis_available'].split(',') if c['diagnosis_available'] else [],

                            biobank=biobank
                        )
                        organizations.append(collection)
           return organizations



    def get_collection_id(self, sample):
        if sample['content_diagnosis'] in ['NCIT:C7772', 'NCIT:C7773', 'NCIT:C7774', 'NCIT:C9036']:
            return 'Sun_Collection_1_Gastric_Carcinome'
        else:
            return 'Sun_Collection_2_Colon_Carcinoma'

    def _generate_sample_disease(self, disease_code):
        disease_ontology_code = DiseaseOntologyCode(
            code=disease_code,
            ontology=DiseaseOntology.ICD_10
        )
        disease = Disease(main_code=disease_ontology_code,mapping_codes=[])
        return [disease]


    def get_cases_data(self)  -> Iterable[Case]:
        with Client(self.emx_2_url) as client:
            client.signin(self.username, self.password)

            # Retrieve signin information
            print(client.status)
            donors = client.get(schema=self.bims_schema, table='SampleDonors')
            # Retrieve data from a table on a schema
            bims_samples = client.get(schema=self.bims_schema, table='Samples')
            cases = []
            for d in donors:
                donor = Donor(id=d['id'],
                              # mapping of the internal gender values to the one used in the model
                              gender=Sex.MALE if d['sex'] == 'M' else Sex.FEMALE,
                              birth_date=d['birth_date'].to_pydatetime()
                )
                samples = []
                for s in bims_samples:
                    if s['donor'] == d['id']:
                        sampling_event = SamplingEvent(id=f"SE-{s['id']}",
                                                       date_at_event=s['creation_datetime'].to_pydatetime()
                                                       )
                        samples.append(Sample(
                            id=s['id'],
                            type=SPECIMENS_MAPPING[s['detailed_sample_type']],
                            events=[sampling_event],
                            content_diagnosis=self._generate_sample_disease(s['content_diagnosis']),
                            collection = Collection( id=self.get_collection_id(s)

                            )
                        ))
                cases.append(Case(
                    donor=donor,
                    samples=samples
                ))
            return cases

if __name__ == '__main__':
    for i in range(1,11):
        source = MolgenisEmx2Source(f'bims-{i}')
        fhir_dest_cases = FHIRDest(JsonFile('./fhir_output'))
        fhir_orgs_cases = FHIRDest(JsonFile('./fhir_orgs_output'))
        converter_orgs = Converter(source, fhir_orgs_cases, Converter.ORGANIZATION)
        converter_orgs.run()
        converter_cases = Converter(source, fhir_dest_cases, Converter.CASE)
        converter_cases.run()