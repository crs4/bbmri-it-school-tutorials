import pandas as pd

from final_project.scripts.bims.sample_types import sample_types
from final_project.scripts.bims.create_bims_data import age_ranges
from final_project.scripts.directory.transcodings import bims_biobanks, bims_collections_diseases, disease_types, \
    sample_types_transcodings


def create_biobank_row (biobank_id, biobank_name):
    biobank =  {
        'id': biobank_id,
        'pid': biobank_id,
        'name': biobank_name,
        'acronym': biobank_id,
        'description': 'biobank_name',
        'url': 'http://example.com',
        'location': '',
        'country': 'IT',
        'latitude': '',
        'longitude': '',
        'head': '',
        'contact': 'bbmri-eric:contactID:EU_network',
        'juridical_person': 'University',
        'network': 'bbmri-eric:networkID:EU_network',
        'combined_network': 'bbmri-eric:networkID:EU_network',
        'also_known': '',
        'collections':'',
        'services': '',
        'quality': '',
        'collaboration_commercial': False,
        'collaboration_non_for_profit': True,
        'national_node': 'EU',
        'withdrawn': False,
        'mg_draft': False
    }
    return biobank

def create_collection_row(collection_id, collection_name, biobank, number_of_donors, diagnosis, age_low, age_high, materials):
    collection = {
    'id': collection_id,
    'name': collection_name,
    'acronym': collection_id,
    'description': collection_name,
    'url': 'http://example.com',
    'location': '',
    'country': 'IT',
    'latitude': '',
    'longitude': '',
    'head': '',
    'contact': 'bbmri-eric:contactID:EU_network',
    'national_node': 'EU',
    'withdrawn': False,
    'parent_collection': '',
    'sub_collections': '',
    'biobank': biobank,
    'biobank_label': biobank,
    'network': 'bbmri-eric:networkID:EU_network',
    'combined_network': '',
    'also_known': '',
    'studies': '',
    'type': 'POPULATION_BASED',
    'data_categories': 'MEDICAL_RECORDS',
    'order_of_magnitude': '2',
    'size': '',
    'categories': '',
    'timestamp': '',
    'quality': '',
    'combined_quality':'',
    'number_of_donors': number_of_donors,
    'order_of_magnitude_donors': '2',
    'sex': '',
    'diagnosis_available': diagnosis,
    'age_low': age_low,
    'age_high': age_high,
    'age_unit': '',
    'facts': '',
    'materials' : materials,
    'storage_temperatures': '',
    'body_part_examined': '',
    'imaging_modality': '',
    'image_dataset_type': '',
    'collaboration_commercial': False,
    'collaboration_non_for_profit': '',
    'data_use': '',
    'duc_profile': '',
    'commercial_use': False,
    'access_fee': '',
    'access_joint_project': '',
    'access_description': '',
    'access_uri': '',
    'sop': '',
    'mg_draft': ''
    }
    return collection

def count_donors_with_diseases(samples_csv_or_df, disease_code_list):
    """
    Count unique donors who have at least one sample with a disease in disease_code_list.

    :param samples_csv_or_df: path to the samples CSV file or a pandas DataFrame
    :param disease_code_list: list of disease codes (e.g., ["NCIT:C7772", "NCIT:C12345"])
    :return: integer count of unique donors
    """
    # Convert list to set for faster lookup
    disease_codes_set = set(disease_code_list)

    # Load samples CSV if a path is given
    if isinstance(samples_csv_or_df, str):
        samples_df = pd.read_csv(samples_csv_or_df)
    else:
        samples_df = samples_csv_or_df.copy()  # assume already a DataFrame

    # Filter samples where content_diagnosis is in the disease set
    filtered_samples = samples_df[samples_df['content_diagnosis'].isin(disease_codes_set)]

    # Get the number of unique donors
    unique_donors_count = filtered_samples['donor'].nunique()

    return unique_donors_count


def create_biobanks_and_collections():
    bb_csv_file = open('Biobanks.csv', 'w')
    bb_csv_file.write('id,pid,name,acronym,description,url,location,country,latitude,longitude,head,contact,juridical_person,network,combined_network,also_known,collections,services,quality,collaboration_commercial,collaboration_non_for_profit,national_node,withdrawn,mg_draft\n')
    collections_csv_file = open('./Collections.csv', 'w')
    collections_csv_file.write('id,name,acronym,description,url,location,country,latitude,longitude,head,contact,national_node,withdrawn,parent_collection,sub_collections,biobank,biobank_label,network,combined_network,also_known,studies,type,data_categories,order_of_magnitude,size,categories,timestamp,quality,combined_quality,number_of_donors,order_of_magnitude_donors,sex,diagnosis_available,age_low,age_high,age_unit,facts,materials,storage_temperatures,body_part_examined,imaging_modality,image_dataset_type,collaboration_commercial,collaboration_non_for_profit,data_use,duc_profile,commercial_use,access_fee,access_joint_project,access_description,access_uri,sop,mg_draft\n')
    for i in range(1, 11):
        biobank_id = bims_biobanks[f'bims_{i}']['biobank_id']
        biobank_name = bims_biobanks[f'bims_{i}']['biobank_name']
        biobank_row = create_biobank_row(biobank_id, biobank_name)
        bb_csv_file.write(f"{biobank_row['id']},{biobank_row['pid']},{biobank_row['name']},{biobank_row['acronym']},{biobank_row['description']},{biobank_row['url']},{biobank_row['location']},{biobank_row['country']},{biobank_row['latitude']},{biobank_row['longitude']},{biobank_row['head']},{biobank_row['contact']},{biobank_row['juridical_person']},{biobank_row['network']},{biobank_row['combined_network']},{biobank_row['also_known']},{biobank_row['collections']},{biobank_row['services']},{biobank_row['quality']},{biobank_row['collaboration_commercial']},{biobank_row['collaboration_non_for_profit']},{biobank_row['national_node']},{biobank_row['withdrawn']},{biobank_row['mg_draft']}\n")
        #generate also the collections for each biobank
        for k in bims_collections_diseases[f'bims_{i}'].keys():
            collection_name = k
            collection_id = f"{biobank_id}_{collection_name.replace(' ', '_')}"
            biobank = biobank_id
            number_of_donors = count_donors_with_diseases(f'../bims/molgenis-emx2/data/bims_{i}/Samples.csv', bims_collections_diseases[f'bims_{i}'][k])
            diagnosis = ','.join(disease_types[d] for d in bims_collections_diseases[f'bims_{i}'][k])
            age_low = age_ranges[f'bims_{i}'][0]
            age_high = age_ranges[f'bims_{i}'][1]
            materials = ','.join(sample_types_transcodings[s['id']] for s in sample_types[f'bims_{i}'])
            collection_row = create_collection_row(collection_id, collection_name, biobank, number_of_donors, diagnosis, age_low, age_high, materials)
            collections_csv_file.write(pd.DataFrame([collection_row]).to_csv(index=False, header=False, lineterminator='\n'))

def main():
    create_biobanks_and_collections()

if __name__ == "__main__":
    main()



