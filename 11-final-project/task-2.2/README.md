# Task 1.2

## Your task objective

1. Create the Fact Table for each of your Collections, starting from the
sample data in your BIMS.
2. Visualize and query the Fact Table in the Directory's Collection page.

## Instructions

The fact table to be created has this structure:

| Column              | Definition                                                      | Label                  | Description                                                                                                                                           |
| ------------------- | ---------------------------------------------------------       | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                  | key=1string required                                            | ID                     | Unique ID of the fact.                                                                                                                                |
| collection          | ref(Collections) required refLabel='${name}'                    | Collection ID          | ID of the collection where the fact belongs to.                                                                                                       |
| sex                 | ontology(DirectoryOntologies.SexTypes) refLabel='${label}'      | Sex                    | The sex of the individuals in the fact. Can be one of the following values: Male, Female, Unknown, Undifferentiated, Not applicable.                  |
| age_range           | ontology(DirectoryOntologies.AgeRanges) refLabel='${label}'     | Age Range              | Age range of the sample donors at time of sample donation.                                                                                            |
| sample_type         | ontology(DirectoryOntologies.MaterialTypes) refLabel='${label}' | Sample Type            | The biospecimen saved from a biological entity for propagation e.g. testing, diagnostics, treatment or research purposes.                             |
| disease             | ref(DirectoryOntologies.DiseaseTypes) refLabel='${label}'       | Disease                | The disease or disease category of main interest in the fact, if any.                                                                                 |
| number_of_samples   | int                                                             | NumberOfSamples        | Number of samples.                                                                                                                                    |
| number_of_donors    | int                                                             | NumberOfDonors         | Number of donors.                                                                                                                                     |
| last_update         | date required                                                   | Date of Last Update    | The date the fact information was last updated in the source system.                                                                                  |
| national_node       | ref(NationalNodes) required refLabel='${description}'           | National Node          | The collection this fact belongs to originates from this national node.                                                                               |


There are four main dimensions for the Fact Table:
 1. sex
 2. age_range
 3. sample_type
 4. disease

The fact table should contain all the possible combinations of these dimensions,
and, for each combination of values, it contains the corresponding number of
samples and donors. The name of the Fact Table in the Directory is
CollectionFacts. Write the output data in a comma-separated value file (CSV), having
as header the column names in the table above.

## Important notes
1. The Fact Table in the Directory is unique for all collections. It is very important
   to choose an ID for each row that is unique across all collections. This could be
   a possible choice for a single row:

       [collection_is]-[sex]-[age_range]-[sample_type]-[disease]

1. The internal codes in your BIMS are not the same used in the Directory. As
   done in the previous task, you will have to map them to the appropriate ones.
   The transcoding table that you used in the previous task
   can be used in this one as well.

3. You can choose your preferred way to create the script for the fact table.
   Notice that the `molgenis-emx2` library can export data from Molgenis as
   Pandas DataFrames. This could be useful to create and compute all the
   aggregations. See <https://molgenis.github.io/molgenis-emx2/#/molgenis/use_usingpyclient>.

## Final checks

Once you have created the CSV file with the Fact Table data, upload it into the
mock Directory. Then, open your Collection(s)'s page and look for the Fact Table at
the bottom.
