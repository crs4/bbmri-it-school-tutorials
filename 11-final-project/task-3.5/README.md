# Task 3.5: add support for updates

## Your task objectives

1. Extend your ETL process to deal with updates to your collections. It should
support the addition of new samples as well as the modification and deletion
of existing samples.
2. Ensure your ETL process is idempotent -- i.e., the execution should result
in the correct representation of your BB metadata through the Bridgehead regardless
of the initial state.
  * E.g., re-running the ETL twice in quick succession should not result in two
    copies of the metadata being loaded.


## Instructions

The most appropriate strategy for achieving your goals may vary depending on how
you implememnted your ETL.
* A simple and robust strategy may be to delete the contents of the FHIR store and reload
  them from scratch.
