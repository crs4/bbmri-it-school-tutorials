# Task 3.6: test support for updates

## Your task objectives

1. Take your original CSV file with the synthetic data and change the Sex of one
   of the participants.
2. Re-run your ETL process.
3. Verify that the change has been propagated to the Sample Locator.


## Instructions

* Re-run the ETL process on the modified dataset, including the import stage
with `blazectl`.
* When it is re-run, the ETL process should generate new JSON files with FHIR resources.
* Importing these into the Bridgehead/BlazeStore should correctly deal with
modifications to resources with a known ID
    * It should also deal with the addition of new resources; deletions would
    need to be dealt in other ways.
