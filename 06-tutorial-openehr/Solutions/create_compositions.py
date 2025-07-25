import json
import copy

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None 



def main():
    #load model composition
    model_composition = read_json_file('composition_modified.json')

    # Load patient data from JSON file
    with open('patients_data.json', 'r') as file:
        patients_data = json.load(file)


    for j, patient in enumerate(patients_data):

        patient_composition = copy.deepcopy(model_composition)
        patient_composition["biobank_report_template/context/biobank/biobank_name"] = patient['biobank_name']
        patient_composition["biobank_report_template/context/biobank/patient_identification/biobank_patient_identifier"]= patient['biobank_patient_identifier']
        patient_composition["biobank_report_template/demographics/birth_summary/date_of_birth"] =str(patient['date_of_birth'])+ "T00:00:00"
        patient_composition["biobank_report_template/demographics/birth_summary/country_of_birth"] = patient['country_of_birth']
        patient_composition["biobank_report_template/demographics/birth_summary/place_of_birth"] = patient['place_of_birth']
        patient_composition["biobank_report_template/demographics/gender/sex_assigned_at_birth"] = patient['sex']
        patient_composition["biobank_report_template/diagnosis/diagnosis/primary_diagnosis"] = patient['primary_diagnosis']
        patient_composition["biobank_report_template/diagnosis/diagnosis/date_of_diagnosis"] = str(patient['date_of_diagnosis']) + "T00:00:00"
        patient_composition["biobank_report_template/diagnosis/diagnosis/timing/specific_event:0/age_at_diagnosis"] = "P"+str(patient['age_at_diagnosis'])+"Y"
        # Process samples
        del patient_composition["biobank_report_template/sample/specimen_summary:0/sample_id/identifier_value|id"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/sample_preservation_mode"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/specimen/sample_material_type"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/specimen/year_of_sample_collection"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/language|code"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/language|terminology"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/encoding|code"]
        del patient_composition["biobank_report_template/sample/specimen_summary:0/encoding|terminology"]
        for i, sample in enumerate(patient['samples']):
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/sample_id/identifier_value|id"] = sample['sample_id']
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/sample_preservation_mode"] = sample['sample_preservation_mode']
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/specimen/sample_material_type"] = sample['sample_material_type']
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/specimen/year_of_sample_collection"] = str(sample['year_of_sample_collection'])+"-01-01T00:00:00"
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/language|code"] = "en"
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/language|terminology"] = "ISO_639-1"
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/encoding|code"] = "UTF-8"
            patient_composition[f"biobank_report_template/sample/specimen_summary:{i}/encoding|terminology"] = "IANA_character-sets"



        with open(f'composition_populated_{j}.json', 'w') as output_file:
            json.dump(patient_composition, output_file, indent=4)

if __name__ == "__main__":
    main()

