from fhirclient import client
from fhirclient.models.patient import Patient

PDQ_SUPPLIER_BASE_URL = "https://gazelle.ihe.net/PatientManager/fhir"

settings = {
    'app_id': 'tet_pdqm_consumer',
    'api_base': PDQ_SUPPLIER_BASE_URL
}

pdqm_consumer_client = client.FHIRClient(settings=settings)

query = Patient.where(struct={
    'family': 'Smith'
})

patients = query.perform_resources(pdqm_consumer_client.server)
print (f'Found {len(patients)} results... parsing and printing')
for patient in patients:
    name = patient.name[0] if patient.name else None
    given = ' '.join(name.given) if name and name.given else ''
    family = name.family if name and name.family else ''
    print ('------------------------------------------------------------------------------------')
    print(f"Patient ID: {patient.id}")
    print(f"Name: {given} {family}")
    print(f"Gender: {patient.gender}")
    print(f"Birthdate: {patient.birthDate.isostring}")
    print ('------------------------------------------------------------------------------------')


