sample_types_transcodings = {
    'LOINC:MTHU029981': 'WHOLE_BLOOD',
    'LOINC:LA30054-3': 'URINE',
    'LOINC:MTHU002157': 'PLASMA',
    'LOINC:LP234849-0': 'TISSUE_FROZEN',
    'LOINC:LP18329-0': 'DNA',
    'LOINC:MTHU001009': 'SERUM',
    'LOINC:MTHU004619': 'SALIVA',
    'LOINC:LA6668-3': 'PATHOGEN',
    'NCIT:C41067': 'WHOLE_BLOOD',
    'NCIT:C13283': 'URINE',
    'NCIT:C13356': 'PLASMA',
    'NCIT:C154905': 'RNA',
    'NCIT:C449': 'DNA',
    'NCIT:C12801': 'TISSUE_FROZEN',
    'NCIT:C13234': 'FECES'
}

disease_types = {
    "NCIT:C7772": "urn:miriam:icd:C16.0",   # Stage I Gastric Cancer → Malignant neoplasm of cardia
    "NCIT:C7773": "urn:miriam:icd:C16.9",   # Stage II Gastric Cancer → Malignant neoplasm of stomach, unspecified
    "NCIT:C7774": "urn:miriam:icd:C16.9",   # Stage III Gastric Cancer → Malignant neoplasm of stomach, unspecified
    "NCIT:C9036": "urn:miriam:icd:C16.9",   # Stage III Gastric Cancer → Malignant neoplasm of stomach, unspecified
    "NCIT:C4910": "urn:miriam:icd:C18",     # Colon Carcinoma → Malignant neoplasm of colon
    "NCIT:C2955": "urn:miriam:icd:C18", # Colorectal Carcinoma → Malignant neoplasm of colon, rectosigmoid junction, and rectum
    "NCIT:C4349": "urn:miriam:icd:C18",     # Colon Adenocarcinoma → Malignant neoplasm of colon
    "NCIT:C43590": "urn:miriam:icd:C18",# Invasive Colorectal Adenocarcinoma → Malignant neoplasm of colon/rectum
    "NCIT:C120083": "urn:miriam:icd:Z80.0", # Lynch Syndrome (Hereditary Colorectal Cancer) → Family history of malignant neoplasm of digestive organs
    "NCIT:C12345": "urn:miriam:icd:M05",    # Rheumatoid Arthritis
    "NCIT:C12346": "urn:miriam:icd:M32",    # Systemic Lupus Erythematosus
    "NCIT:C12347": "urn:miriam:icd:G35",    # Multiple Sclerosis
    "NCIT:C12348": "urn:miriam:icd:E10",    # Type 1 Diabetes Mellitus
    "NCIT:C12349": "urn:miriam:icd:E05.0",  # Graves' Disease → Thyrotoxicosis with diffuse goiter
    "NCIT:C12350": "urn:miriam:icd:E84",    # Cystic Fibrosis
    "NCIT:C12351": "urn:miriam:icd:G71.0",  # Duchenne Muscular Dystrophy
    "NCIT:C12352": "urn:miriam:icd:G10",    # Huntington's Disease
    "NCIT:C12353": "urn:miriam:icd:Q87.4",  # Marfan Syndrome
    "NCIT:C12354": "urn:miriam:icd:Q85.0",  # Neurofibromatosis Type 1
    "NCIT:C195126": "urn:miriam:icd:E10-E14",   # Diabetes Mellitus due to underlying condition
    "NCIT:C99532": "urn:miriam:icd:Z13.1",  # Long term insulin therapy (diabetes therapy)
    "NCIT:C129739": "urn:miriam:icd:E10",   # Type 1 Diabetes Mellitus
    "NCIT:C26747": "urn:miriam:icd:E11",    # Type 2 Diabetes Mellitus
    "NCIT:C212171": "urn:miriam:icd:B18.1", # Chronic Hepatitis B
    "NCIT:C144153": "urn:miriam:icd:B19.9", # Viral Hepatitis, unspecified
    "NCIT:C35124": "urn:miriam:icd:B19",    # Viral Hepatitis, unspecified
    "NCIT:C3096": "urn:miriam:icd:B15",     # Hepatitis A
    "NCIT:C194020": "urn:miriam:icd:B19.9", # Unspecified Viral Hepatitis without Hepatic Coma
    "NCIT:C4872": "urn:miriam:icd:C50",     # Breast carcinoma
    "NCIT:C116977": "urn:miriam:icd:D05",   # Carcinoma in situ of breast
    "NCIT:C138986": "urn:miriam:icd:C50",   # Prognostic factors in breast cancer → Breast cancer (general)
    "NCIT:C60893": "urn:miriam:icd:C56",    # Ovarian Cancer (pM0) → Malignant neoplasm of ovary
    "NCIT:C60895": "urn:miriam:icd:C56",    # Ovarian Cancer (pM1) → Malignant neoplasm of ovary
    "COVID-19-VIR": "urn:miriam:icd:U07.1",  # COVID-19, virus identified
    "COVID-19-UNK": "urn:miriam:icd:U07.2",  # COVID-19, virus not identified
    "COVID-19-DISEASE": "urn:miriam:icd:U07.1",  # Disease caused by COVID-19
    "CYSTIC-FIBROSIS": "urn:miriam:icd:E84",  # Cystic Fibrosis
    "SPM-ARTR": "urn:miriam:icd:G12.1",  # Spinal muscular atrophy
    "DM-DIST": "urn:miriam:icd:G71.0",  # Duchenne muscular dystrophy
    "XL-SPI": "urn:miriam:icd:G12.1",  # X-linked spinal muscular atrophy (SMAX2)
    "PRX-SPI": "urn:miriam:icd:G12.1"
}

sex = {
    'M': 'MALE',
    'F': 'FEMALE',
    'O': 'OTHER'
}

bims_diseases_collections = {
'bims_1':
    {'NCIT:C7772': 'Collection 1 Gastric Carcinome',
    'NCIT:C7773': 'Collection 1 Gastric Carcinome',
    'NCIT:C7774': 'Collection 1 Gastric Carcinome',
    'NCIT:C9036': 'Collection 1 Gastric Carcinome',
    'NCIT:C4910': 'Collection 2 Colon Carcinoma',
    'NCIT:C2955': 'Collection 2 Colon Carcinoma',
    'NCIT:C4349': 'Collection 2 Colon Carcinoma',
    'NCIT:C43590': 'Collection 2 Colon Carcinoma',
    'NCIT:C120083': 'Collection 2 Colon Carcinoma',

    },
'bims_6':
{'NCIT:C7772': 'Collection 1 Gastric Carcinome',
 'NCIT:C7773': 'Collection 1 Gastric Carcinome',
 'NCIT:C7774': 'Collection 1 Gastric Carcinome',
 'NCIT:C9036': 'Collection 1 Gastric Carcinome',
 'NCIT:C4910': 'Collection 2 Colon Carcinoma',
 'NCIT:C2955': 'Collection 2 Colon Carcinoma',
 'NCIT:C4349': 'Collection 2 Colon Carcinoma',
 'NCIT:C43590': 'Collection 2 Colon Carcinoma',
 'NCIT:C120083': 'Collection 2 Colon Carcinoma',

 },

'bims_2':
    {'COVID-19-VIR' : 'Collection 1 COVID-19 ',
        'COVID-19-UNK' : 'Collection 1 COVID-19 ',
        'COVID-19-DISEASE' : 'Collection 1 COVID-19 ',
        'CYSTIC-FIBROSIS' : 'Collection 2 Rare Diseases',
        'SPM-ARTR' : 'Collection 2 Rare Diseases',
        'DM-DIST' : 'Collection 2 Rare Diseases',
        'XL-SPI' : 'Collection 2 Rare Diseases',
        'PRX-SPI' : 'Collection 2 Rare Diseases'
    },

'bims_7':
    {'COVID-19-VIR' : 'Collection 1 COVID-19 ',
        'COVID-19-UNK' : 'Collection 1 COVID-19 ',
        'COVID-19-DISEASE' : 'Collection 1 COVID-19 ',
        'CYSTIC-FIBROSIS' : 'Collection 2 Rare Diseases',
        'SPM-ARTR' : 'Collection 2 Rare Diseases',
        'DM-DIST' : 'Collection 2 Rare Diseases',
        'XL-SPI' : 'Collection 2 Rare Diseases',
        'PRX-SPI' : 'Collection 2 Rare Diseases'
    },

'bims:3': {
    'NCIT:C12345': 'Collection 1 Autoimmune and Genetic Diseases',
    'NCIT:C12346': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12347': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12348': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12349': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12351': 'Collection 2 Rare Diseases',
    'NCIT:C12352': 'Collection 2 Rare Diseases',
    'NCIT:C12353': 'Collection 2 Rare Diseases',
    'NCIT:C12354': 'Collection 2 Rare Diseases',
}  ,
    'bims:8': {
    'NCIT:C12345': 'Collection 1 Autoimmune and Genetic Diseases',
    'NCIT:C12346': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12347': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12348': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12349': 'Collection 1 Autoimmune and genetic Diseases',
    'NCIT:C12351': 'Collection 2 Rare Diseases',
    'NCIT:C12352': 'Collection 2 Rare Diseases',
    'NCIT:C12353': 'Collection 2 Rare Diseases',
    'NCIT:C12354': 'Collection 2 Rare Diseases',
},
    'bims_4' : {
    'NCIT:C195126': 'Collection 1 Diabetes',
    'NCIT:C99532': 'Collection 1 Diabetes',
    'NCIT:C129739': 'Collection 1 Diabetes',
    'NCIT:C26747': 'Collection 1 Diabetes',
    'NCIT:C212171': 'Collection 2 Hepatitis',
    'NCIT:C144153': 'Collection 2 Hepatitis',
    'NCIT:C35124': 'Collection 2 Hepatitis',
    'NCIT:C3096': 'Collection 2 Hepatitis',
    'NCIT:C194020': 'Collection 2 Hepatitis'
    },
    'bims_9' : {
    'NCIT:C195126': 'Collection 1 Diabetes',
    'NCIT:C99532': 'Collection 1 Diabetes',
    'NCIT:C129739': 'Collection 1 Diabetes',
    'NCIT:C26747': 'Collection 1 Diabetes',
    'NCIT:C212171': 'Collection 2 Hepatitis',
    'NCIT:C144153': 'Collection 2 Hepatitis',
    'NCIT:C35124': 'Collection 2 Hepatitis',
    'NCIT:C3096': 'Collection 2 Hepatitis',
    'NCIT:C194020': 'Collection 2 Hepatitis'
    },
    'bims_5': {
               'NCIT:C4872': 'Collection 1 Breast Carcinoma',
                'NCIT:C116977': 'Collection 1 Breast Carcinoma',
                'NCIT:C138986': 'Collection 1 Breast Carcinoma',
                'NCIT:C60893': 'Collection 2 Ovarian Cancer',
                'NCIT:C60895': 'Collection 2 Ovarian Cancer'


    },
    'bims_10': {
        'NCIT:C4872': 'Collection 1 Breast Carcinoma',
        'NCIT:C116977': 'Collection 1 Breast Carcinoma',
        'NCIT:C138986': 'Collection 1 Breast Carcinoma',
        'NCIT:C60893': 'Collection 2 Ovarian Cancer',
        'NCIT:C60895': 'Collection 2 Ovarian Cancer'

    }
}



bims_biobanks = {
    'bims_1' : {
        'biobank_id': 'Sun',
        'biobank_name': 'Colon and Gastrc carcinoma Biobank - Sun'
               },
    'bims_2' : {
        'biobank_id': 'Mercury',
        'biobank_name': 'Rare Diseases and COVID-19 Biobank - Mercury'
                },
    'bims_3' : {
        'biobank_id': 'Venus',
        'biobank_name': 'Autoimmune Genetic Diseases and Rare Diseases Biobank - Venus'
                },
    'bims_4' : {
        'biobank_id': 'Earth',
        'biobank_name': 'Diabetes and Hepatitis Biobank - Earth'
                },
    'bims_5' : {
        'biobank_id': 'Moon',
        'biobank_name': 'Breast and Ovarian Cancer Biobank - Moon'
                },
    'bims_6' : {
        'biobank_id': 'Mars',
        'biobank_name': 'Colon and Gastrc carcinoma Biobank - Mars'
                },
    'bims_7' : {
        'biobank_id': 'Jupiter',
        'biobank_name': 'Rare Diseases and COVID-19 Biobank - Jupiter'
                },
    'bims_8' : {
        'biobank_id': 'Saturn',
        'biobank_name': 'Autoimmune Genetic Diseases and Rare Diseases Biobank - Saturn'
                },
    'bims_9' : {
        'biobank_id': 'Uranus',
        'biobank_name': 'Diabetes and Hepatitis Biobank - Uranus'
                },
    'bims_10' : {
        'biobank_id': 'Neptune',
        'biobank_name': 'Breast and Ovarian Cancer Biobank - Neptune'
    }

}

bims_collections_diseases = {
    'bims_1': {
        'Collection 1 Gastric Carcinome': ['NCIT:C7772', 'NCIT:C7773', 'NCIT:C7774', 'NCIT:C9036'],
        'Collection 2 Colon Carcinoma': ['NCIT:C4910', 'NCIT:C2955', 'NCIT:C4349', 'NCIT:C43590', 'NCIT:C120083']
    },
    'bims_6': {
        'Collection 1 Gastric Carcinome': ['NCIT:C7772', 'NCIT:C7773', 'NCIT:C7774', 'NCIT:C9036'],
        'Collection 2 Colon Carcinoma': ['NCIT:C4910', 'NCIT:C2955', 'NCIT:C4349', 'NCIT:C43590', 'NCIT:C120083']
    },
    'bims_2': {
        'Collection 1 COVID-19 ': ['COVID-19-VIR', 'COVID-19-UNK', 'COVID-19-DISEASE'],
        'Collection 2 Rare Diseases': ['CYSTIC-FIBROSIS', 'SPM-ARTR', 'DM-DIST', 'XL-SPI', 'PRX-SPI']
    },
    'bims_7': {
        'Collection 1 COVID-19 ': ['COVID-19-VIR', 'COVID-19-UNK', 'COVID-19-DISEASE'],
        'Collection 2 Rare Diseases': ['CYSTIC-FIBROSIS', 'SPM-ARTR', 'DM-DIST', 'XL-SPI', 'PRX-SPI']
    },
    'bims_3': {
        'Collection 1 Autoimmune and Genetic Diseases': ['NCIT:C12345', 'NCIT:C12346', 'NCIT:C12347', 'NCIT:C12348', 'NCIT:C12349'],
        'Collection 2 Rare Diseases': ['NCIT:C12351', 'NCIT:C12352', 'NCIT:C12353', 'NCIT:C12354']
    },
    'bims_8': {
        'Collection 1 Autoimmune and Genetic Diseases': ['NCIT:C12345', 'NCIT:C12346', 'NCIT:C12347', 'NCIT:C12348', 'NCIT:C12349'],
        'Collection 2 Rare Diseases': ['NCIT:C12351', 'NCIT:C12352', 'NCIT:C12353', 'NCIT:C12354']
    },
    'bims_4': {
        'Collection 1 Diabetes': ['NCIT:C195126', 'NCIT:C99532', 'NCIT:C129739', 'NCIT:C26747'],
        'Collection 2 Hepatitis': ['NCIT:C212171', 'NCIT:C144153', 'NCIT:C35124', 'NCIT:C3096', 'NCIT:C194020']
    },
    'bims_9': {
        'Collection 1 Diabetes': ['NCIT:C195126', 'NCIT:C99532', 'NCIT:C129739', 'NCIT:C26747'],
        'Collection 2 Hepatitis': ['NCIT:C212171', 'NCIT:C144153', 'NCIT:C35124', 'NCIT:C3096', 'NCIT:C194020']
    },
    'bims_5': {
        'Collection 1 Breast Carcinoma': ['NCIT:C4872', 'NCIT:C116977', 'NCIT:C138986'],
        'Collection 2 Ovarian Cancer': ['NCIT:C60893', 'NCIT:C60895']
    },
    'bims_10': {
        'Collection 1 Breast Carcinoma': ['NCIT:C4872', 'NCIT:C116977', 'NCIT:C138986'],
        'Collection 2 Ovarian Cancer': ['NCIT:C60893', 'NCIT:C60895']
    }
}


