# Task 1.1: create your biobank

## Your task objective

Give your biobank a sample metadata management system and load it with data. At the end of the task each participant should have his/her own Molgenis instance implementing a BIMS, with test data loaded.

## Description of the test BIMS schema.

The BIMS schema that you're going to load on your Molgenis instance is composed by the following tables (Entities):
- `AnatomicalSitesOntology`: ontology table that provides all the anatomical site codes used in the BIMS;
- `ConsentDecisionsOntology`: ontology table that provides all the CCE codes used in the BIMS, to represent Consents Decision;
- `ConsentsConditionsOntology`: ontology table for the Consent Decision values (PERMIT/DENY);
- `DiagnosysOntology`: ontology table that provides all the diagnosis codes used in the BIMS;
- `SampleConsents`: table that, for all or some samples registered in the BIMS, provides the Consent Decision information;
- `SampleDonors`: demographics table for the sample donors (date of birth, sex and donor id);
- `SampleTypesOntology`: ontology table that provides all the sample type codes used in the BIMS;
- `Samples`: table that provides all the sample information (type, anatomical site, diagnosis, donor, etc);
- `SexOntology`: ontology table that provides the codes for gender used in the BIMS.


## Instructions

1. Deploy an instance of Molgenis, using Docker, on your biobank's dedicated VM using the docker-compose.bims.yml file at Navigate to the [BIMS data folder](https://space.crs4.it/s/CA2ZXRbJmHStm95).
    * Your instance should be accessible at port 8080 of your VM. You'll need to create an SSH bridge to access it via localhost since the port is not exposed outside. To do that add the option `-L 8080:127.0.0.1:8080` to your ssh command. For example:
```
   ssh -i ~/.ssh/your-key -L 8080:127.0.0.1:8080 ubuntu@ec2-54-220-181-93.eu-west-1.compute.amazonaws.com
```
    * ⚠️ **Warning**. Change the default admin account password immediately!! Your VM is accessible from the internet.
2. Enter your biobank's organizational information into Molgenis, so that it will be available when querying or extracting metadata.
3. The datasets provided for the test BIMS used in this final project (yours is one of these) are described in the following table:

| BIMS         | Disease Types                            | Population Age   | Possible Collections                                                    | Terminologies                                                              |
| ---------    | ---------------------------------------- | ---------------- | ----------------------------------------------------------------------- | --------------------------------------------------                         |
| BB-Sun     | Cancer (gastric and colon)               | 0–99             | 1 for Gastric, 1 for colon                                              | LOINC for Sample types, NCIT for diseases                                  |
| BB-Mercury | Cancer (gastric and colon)               | 75–99            | 1 for Gastric, 1 for colon                                              | LOINC for Sample types, NCIT for diseases                                  |
| BB-Venus   | Rare diseases and COVID-19               | 0–99             | 1 for rare diseases, 1 for COVID-19                                     | LOINC for sample types, internal coding for COVID-19 and for rare diseases |
| BB-Earth   | Rare diseases and COVID-19               | 75–99            | 1 for rare diseases, 1 for COVID-19                                     | LOINC for sample types, internal coding for COVID-19 and for rare diseases |
| BB-Moon    | Autoimmune, genetic, and rare diseases   | 0–18             | 1 for autoimmune, 1 for genetics                                        | NCIT for sample types, NCIT for diseases                                   | | BB-Mars    | Autoimmune, genetic, and rare diseases   | 75–99            | 1 for autoimmune, 1 for genetics                                        | NCIT for sample types, NCIT for diseases                                   |
| BB-Jupiter | Diabetes and Hepatitis study             | 18–45            | One for each of the two studies                                         | NCIT for sample types, LOINC for diseases                                  |
| BB-Saturn  | Diabetes and Hepatitis study             | 75–99            | One for each of the two studies                                         | NCIT for sample types, LOINC for diseases                                  |
| BB-Uranus  | Breast Cancer – Ovary Cancer             | 18–45            | One for each of the two cancer types                                    | LOINC for Sample types, NCIT for diseases                                  |
| BB-Neptune | Breast Cancer – Ovary Cancer             | 75–99            | One for each of the two cancer types                                    | LOINC for Sample types, NCIT for diseases                                  |

As you see the BIMS are paired. For each pair, the BBs have the same sample type
and they are different on in the age of their populations.

**You and your neighbour should be working on paired BBs**; your collection metadata
will be different, but since the data type/schemas are the same you will be able
to collaborate and share on  all code.

4. Navigate to the [BIMS data folder](https://space.crs4.it/s/CA2ZXRbJmHStm95).
    * Download the `molgenis.csv` file from root directory.
    * Go into the directory for your assigned biobank.
5. From the Molgenis interface, create a schema for your BIMS, give it the name you prefer, and do not select any template.
6. Once the schema is created, click on it to open the schema configuration page
   and go to the Up/Download button. Upload the `molgenis.csv` file, to create the tables schema.
7. Now Upload all the `.csv` data files in the data directory dedicated to your BB, starting from those in
   the Ontology folder, then Donors and Samples at the end. This will populate
   all the tables with test data.
8. From the Tables tab, now explore the data you have just loaded in Molgenis to ensure the
   operation completed successfully.
