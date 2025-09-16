#Some suggestions about how to extraxt data from the molgenis emx2 database and make operations of
#transformations and aggregations

from molgenis_emx2_pyclient import Client
EMX_2_URL = "your_molgenis_url"

disease_transcodings = {} #your diseses transcodings

with Client(EMX_2_URL) as client:
    client.signin('admin', 'admin')

    #get your entity values as pandas dataframe
    samples = client.get(schema='bims-1', table='Samples', as_df=True)
    donors = client.get(schema='bims-1', table='SampleDonors', as_df=True)

    #applytranscodings to your dataframe columns
    samples['content_diagnosis'] = samples['content_diagnosis'].map(disease_transcodings)

    #join the two dataframes to add donors age to the samples dataframe
    samples = samples.merge(donors[["id", "birth_date"]], left_on="donor", right_on="id", how="left")

    #filter a dataframe accorfing to a column values
    samples= samples[samples["content_diagnosis"].isin(['NCIT:C7772', 'NCIT:C7773', 'NCIT:C7774', 'NCIT:C9036'])]

    