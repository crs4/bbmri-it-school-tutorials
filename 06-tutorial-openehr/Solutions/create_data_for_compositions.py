import random
from datetime import date
import calendar
import json

CITIES_IT = [
    "Roma",
    "Milano",
    "Napoli",
    "Torino",
    "Palermo",
    "Genova",
    "Bologna",
    "Firenze",
    "Cagliari",
    "Bari",
    "Venezia",
]

CITIES_DE = [
    "Berlin",
    "Hamburg",
    "Munich",
    "Cologne",
    "Frankfurt",
    "Stuttgart",
    "Düsseldorf",
    "Dortmund",
    "Essen",
    "Leipzig",
]

CITIES_FR = [
    "Paris",
    "Lyon",
    "Marseille",
    "Toulouse",
    "Nice",
    "Nantes",
    "Strasbourg",
    "Montpellier",
    "Bordeaux",
    "Lille",
]

biobanks=[
    {"id":"01","name":"FirstBiobank","country": "Italy","acronym": "FB","cities": CITIES_IT},
    {"id":"02","name":"SecondBiobank","country": "Germany","acronym": "SB","cities": CITIES_DE},
    {"id":"03","name":"ThirdBiobank","country": "France","acronym": "TB","cities": CITIES_FR}
]

material_type=["Tumor tissue sample"]

preservation = ['FFPE','Cryopreservation']

def get_biobank_name(biobank):
    return biobank['name']

def get_biobank_patient_identifiers(biobank,number):
    return [biobank['acronym']+str(idx) for idx in range(1,number+1)]

def get_place_of_birth(biobank):
    return random.choice(biobank["cities"])

def get_birth_date():
    return get_random_date(1950,2010)

def get_random_date(start,end):
    year = random.randint(start, end)
    month = random.randint(1, 12)
    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif month == 2:
        if calendar.isleap(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)

    date_of_birth = date(
        year=year,
        month=month,
        day=day,
    )
    return date_of_birth

def get_country_of_birth(biobank):
    return biobank['country']


def get_number_patients_per_biobank(ntotal):
    nbiobanksfractions=[0.5,0.3,0.2]
    return [int(n*ntotal) for n in nbiobanksfractions]
    
def get_sex():
    return random.choice(['M','F'])

def get_primary_diagnosis(sex):
    diagnosis_m=['Lung Cancer','Colorectal Cancer']
    diagnosis_f=['Breast Cancer','Colorectal Cancer']
    if (sex == 'M'):
        diagnosis=diagnosis_m
    else:
        diagnosis=diagnosis_f
    return random.choice(diagnosis)

def get_date_of_diagnosis(dob):
    return get_random_date(dob.year+10,max(dob.year+10,2015))

def age_at_diagnosis(dob,date_of_diagnosis):
    return date_of_diagnosis.year-dob.year

def get_material_type():
    return material_type[0]

def get_preservation_mode():
    return random.choice(preservation)

def get_year_sample_collection(date_of_diagnosis):
    return get_random_date(date_of_diagnosis.year, date_of_diagnosis.year+10).year

def main():
    ntotal=50 # total number of patients to generate
    nbiobanks=get_number_patients_per_biobank(ntotal)
    patients = []
    for idx, bb in enumerate(biobanks):
        npatients = nbiobanks[idx]
        biobank_name = get_biobank_name(bb)
        biobank_patient_identifiers = get_biobank_patient_identifiers(bb, npatients)
        for i,patient_id in enumerate(biobank_patient_identifiers):
            dob = get_birth_date()
            country_of_birth = get_country_of_birth(bb)
            place_of_birth = get_place_of_birth(bb)
            pid=biobank_patient_identifiers[i]
            sex = get_sex()
            primary_diagnosis = get_primary_diagnosis(sex)
            date_of_diagnosis = get_date_of_diagnosis(dob)
            age = age_at_diagnosis(dob, date_of_diagnosis)
            nsamples=random.randint(0, 3)  # number of samples per patient
            samples=[]
            for j in range(nsamples):
                sample_id = f"{pid}_{j+1}"
                sample_material_type = get_material_type()
                sample_preservation_mode = get_preservation_mode()
                year_sample_collection = get_year_sample_collection(date_of_diagnosis)
                
                samples.append({
                    "sample_id": sample_id,
                    "sample_material_type": sample_material_type,
                    "sample_preservation_mode": sample_preservation_mode,
                    "year_of_sample_collection": year_sample_collection
                })
            patient_data = {
                "biobank_name": biobank_name,
                "biobank_patient_identifier": pid,
                "date_of_birth": dob,
                "country_of_birth": country_of_birth,
                "place_of_birth": place_of_birth,
                "sex": sex,
                "primary_diagnosis": primary_diagnosis,
                "date_of_diagnosis": date_of_diagnosis,
                "age_at_diagnosis": age,
                "samples": samples
            }
            patients.append(patient_data)
    with open("patients_data.json", "w") as f:
        json.dump(patients, f, indent=4, default=str)

if __name__ == "__main__":
    main()  