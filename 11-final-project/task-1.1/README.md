# Task 1.1

## Your task objective

Give your biobank a sample metadata management system and load it with data. At the ens of the task each participant should have its own Molgenis instance implementing a BIMS, with test data loaded. 

## Description of the test BIMS schema. 

The BIMS schema of test on Molgenis is composed by the following tables (Entities):
- AnatomicalSitesOntology: Ontology table that provides all thr anatomicl site codes used in the BIMS	
- ConsentDecisionsOntology: Ontology table that provides all the CCEs codes used in the BIMS to provide Consents Decision
- ConsentsConditionsOntology: Ontology table for the Consent decision values (PERMIT/DENY)	
- DiagnosysOntology: Ontology table that provides all the diagnosis codes used in the BIMS
- SampleConsents: Table that for all or some samples registered in the bims provides the consent decision information
- SampleDonors: Demogrhaphics table for the sample donors (date of birth, sex and donor id)
- SampleTypesOntology: Ontologu table that provides all the sample type codes used in the BIMS
- Samples: Table that provides all the sample information (type, anatomical site, diagnosis, donor, etc)	
- SexOntology: Ontology table that provides the codes for gender used in the BIMS


## Instructions

1. Deploy an instance of MOLGENIS, using Docker, on your biobank's dedicated VM.
2. Enter your biobank's organizational information into MOLGENIS, so that it will be available when querying or extracting metadata.
3. Pick one of the provided test BIMS. The details of the BIMS are provided in the following table:


| BIMS    | Disease Types                          | Population Age | Possible Collections                                                  | Terminologies                                     |
|---------|----------------------------------------|----------------|-----------------------------------------------------------------------|--------------------------------------------------|
| bims_1  | Cancer (gastric and colon)             | 0–99           | 1 for Gastric, 1 for colon                                            | LOINC for Sample types, NCIT for diseases        |
| bims_2  | Cancer (gastric and colon)             | 75–99          | 1 for Gastric, 1 for colon                                            | LOINC for Sample types, NCIT for diseases        |
| bims_3  | Rare diseases and COVID-19             | 0–99           | 1 for rare diseases, 1 for COVID-19                                   | LOINC for sample types, internal coding for COVID-19 and for rare diseases |
| bims_4  | Rare diseases and COVID-19             | 75–99          | 1 for rare diseases, 1 for COVID-19                                   | LOINC for sample types, internal coding for COVID-19 and for rare diseases |
| bims_5  | Autoimmune, genetic, and rare diseases | 0–18           | 1 for autoimmune, 1 for genetics                                      | NCIT for sample types, NCIT for diseases         |
| bims_6  | Autoimmune, genetic, and rare diseases | 75–99          | 1 for autoimmune, 1 for genetics | NCIT for sample types, NCIT for diseases         |
| bims_7  | Diabetes and Hepatitis study           | 18–45          | One for each of the two studies                                       | NCIT for sample types, LOINC for diseases        |
| bims_8  | Diabetes and Hepatitis study           | 75–99          | One for each of the two studies                                       | NCIT for sample types, LOINC for diseases        |
| bims_9  | Breast Cancer – Ovary Cancer           | 18–45          | One for each of the two cancer types                                  | LOINC for Sample types, NCIT for diseases        |
| bims_10 | Breast Cancer – Ovary Cancer           | 75–99          | One for each of the two cancer types                                  | LOINC for Sample types, NCIT for diseases        |

 As you see the BIMS are paired, so you can pick up one of the two BIMS in each pair according to your table neighbor.

4. Download the molgenis.csv file and thefolder containing the data for the BIMS you picked, from here: [BIMS data folder](https://space.crs4.it/apps/files/files/3876464?dir=/Shared/Scuola_BBMRI.it/Material%20Final%20Project/BIMS)

5. From the Molgenis interface, create a schema for your BIMS, give it the name you prefere, and do not select any template. 
6. Once the schema is created, click on it to open the schema configuration page and go to the Up/Download button, upload the molgenis.csv file, to create the tables schema 
7. Now Upload all the .csv files in the bims_* directory, starting from those in the Ontology folder, then Donors and Samples at the end. This will populate all the tables with test data
8. From the Tables tab, you can now explore the data you have just loaded

### Relevant lab setup

Use the VM which you have been assigned.  Create your deployment on it.

⚠️ **Note**. DO NOT KEEP default account passwords -- your VM is accessible from the internet.