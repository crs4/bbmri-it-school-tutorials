#Some suggestions about how to extraxt data from the molgenis emx2 database and make operations of
#transformations and aggregations

from molgenis_emx2_pyclient import Client
EMX_2_URL = "your_molgenis_url"

disease_transcodings = {} #your diseses transcodings

age_range_categories = {
    'Infant': (0, 2),
    'Child': (2, 13),
    'Adolescent': (13, 18),
    'Young Adult': (18, 25),
    'Adult': (25, 45),
    'Middle-aged': (45, 65),
    'Aged (65-79 years)': (65, 80),
    'Aged (>80 years)': (80, 150)
}

def categorize_age(age: int, age_ranges: dict) -> str:

    for category, (min_age, max_age) in age_ranges.items():
        if min_age <= age < max_age:
            return category
    return "Unknown"  # fallback if not found

with Client(EMX_2_URL) as client:
    client.signin('admin', 'admin')

    #get your entity values as pandas dataframe
    samples = client.get(schema='bims-1', table='Samples', as_df=True)
    donors = client.get(schema='bims-1', table='SampleDonors', as_df=True)

    #applytranscodings to your dataframe columns
    samples['content_diagnosis'] = samples['content_diagnosis'].map(disease_transcodings)

    #join the two dataframes to add donors age to the samples dataframe
    samples = samples.merge(donors[["id", "birth_date"]], left_on="donor", right_on="id", how="left")

    #filter a dataframe according to a column values
    samples= samples[samples["content_diagnosis"].isin(['NCIT:C7772', 'NCIT:C7773', 'NCIT:C7774', 'NCIT:C9036'])]

    #get all the unique values of a column
    diseases= samples['content_diagnosis'].unique()

    #rename a column
    samples = samples.rename(columns={"birth_date": "age"})

    #replace a column with the result of a function applied to each value of the column.
    samples['age'] = samples['age'].apply(lambda x: categorize_age(x, age_range_categories))
