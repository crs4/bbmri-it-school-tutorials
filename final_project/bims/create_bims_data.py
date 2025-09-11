from population_age_range import random_dob
from population_gender import pick_gender
from sample_types import sample_types
import random
from datetime import date, timedelta
from diseases import diseases

population = {'bims_1': 600,
              'bims_2': 1200,
              'bims_3': 300,
              'bims_4': 1500,
              'bims_5': 750,
              'bims_6': 600,
              'bims_7': 1200,
              'bims_8': 300,
              'bims_9': 1500,
              'bims_10': 750
              }

samples = { 'bims_1': 900,
            'bims_2': 1800,
            'bims_3': 450,
            'bims_4': 2250,
            'bims_5': 1125,
            'bims_6': 900,
            'bims_7': 1800,
            'bims_8': 450,
            'bims_9': 2250,
            'bims_10': 1125
}

male_rates = {'bims_1': 0.25,
                'bims_2': 0.5,
                'bims_3': 0.7,
                'bims_4': 0.85,
                'bims_5': 0,
                'bims_6': 0.25,
                'bims_7': 0.5,
                'bims_8': 0.7,
                'bims_9': 0.85,
                'bims_10': 0
    }

age_ranges = {
    'bims_1': (0, 99),
    'bims_2': (0, 99),
    'bims_3': (0, 18),
    'bims_4': (18, 45),
    'bims_5': (18, 45),
    'bims_6': (75, 99),
    'bims_7': (75, 99),
    'bims_8': (75, 99),
    'bims_9': (75, 99),
    'bims_10': (75, 99),

}




def random_date(start_year=2018, end_year=2024):
    """
    Pick a random date between January 1st of start_year
    and December 31st of end_year.
    Each year has equal probability of being chosen.
    Returns: string in YYYY-MM-DD format.
    """
    # Step 1: choose a random year
    year = random.randint(start_year, end_year)

    # Step 2: calculate number of days in the chosen year
    first_day = date(year, 1, 1)
    first_day_next_year = date(year + 1, 1, 1)
    days_in_year = (first_day_next_year - first_day).days

    # Step 3: pick a random offset
    random_day_offset = random.randint(0, days_in_year - 1)

    # Step 4: return formatted string
    return (first_day + timedelta(days=random_day_offset)).strftime("%Y-%m-%d")


def generate_donors():
    csv_header = 'id, birth_date, sex'
    for i in range(1,11):
        print(f'bims_{i}')
        bims_donors_out = open(f'./bims/molgenis-emx2/data/bims_{i}/SampleDonors.csv', 'w')
        bims_donors_out.write(csv_header+'\n')
        for j in range(1, population[f'bims_{i}'] + 1):
            donor_id = f'DONOR-BIMS-{i}-{j:04d}'
            birth_date = random_dob(age_ranges[f'bims_{i}'][0], age_ranges[f'bims_{i}'][1])
            sex = pick_gender(male_rates[f'bims_{i}'])
            bims_donors_out.write(f'{donor_id},{birth_date},{sex}\n')
        bims_donors_out.close()

def generate_samples():
    csv_header = 'id, detailed_sample_type,storage_temperature,creation_datetime,anatomical_site,content_diagnosis,donor'
    for i in range(1,11):
        print(f'bims_{i}')
        bims_samples_out = open(f'./bims/molgenis-emx2/data/bims_{i}/Samples.csv', 'w')
        bims_samples_out.write(csv_header+'\n')
        for j in range(1, samples[f'bims_{i}'] + 1):
            sample_type = random.choice(sample_types[f'bims_{i}'])
            sample_id = f'SAMPLE-BIMS-{i}-{j:04d}'
            sample_type = random.choice(sample_types[f'bims_{i}'])
            detailed_sample_type =sample_type['id']
            anatomical_site = sample_type['anatomical_site']
            storage_temperature = sample_type['storage_temp']
            creation_datetime = random_date()
            content_diagnosis = random.choice(diseases[f'bims_{i}'])['id']
            #ensure that each donor has at least one sample
            if j in range (1,  population[f'bims_{i}'] + 1):
                donor_id = f'DONOR-BIMS-{i}-{j:04d}'
            else:
                donor_id = f'DONOR-BIMS-{i}-{random.randint(1, population[f"bims_{i}"]):04d}'
            bims_samples_out.write(f'{sample_id},{detailed_sample_type},{storage_temperature},{creation_datetime},{anatomical_site},{content_diagnosis},{donor_id}\n')
        bims_samples_out.close()



def main():
    generate_donors()
    generate_samples()

if __name__ == '__main__':
    main()