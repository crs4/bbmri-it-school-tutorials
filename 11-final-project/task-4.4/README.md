# Task 4.4: Create a Workflow RO-Crate for your ETL workflow

## Your task objective

1. Create a Workflow RO-Crate for your ETL workflow with
   [ro-crate-py](https://github.com/ResearchObject/ro-crate-py)
2. Validate your Workflow RO-Crate with the [RO-Crate
   validator](https://github.com/crs4/rocrate-validator)

## Instructions

## Part 1

We will assume that your workflow -- or the main entry point of your workflow
-- is a Python script called `etl.py`, located in a directory called
`etl_workflow` (this directory might contain additional files that your
workflow needs). In the following, replace this with your actual (main)
workflow file.

* Install ro-crate-py and use the `rocrate` tool to initialize the
  `etl_workflow` directory as an RO-Crate.
* Use the `rocrate` tool to add the `etl.py` file to the metadata as a
  workflow.

## Part 2

* Install the RO-Crate validator and use the `rocrate-validator` tool to
  validate the RO-Crate at the `REQUIRED` level (the default).
* The validator should report that the RO-Crate is invalid because the Root
  Data Entity is missing some properties. Open the `ro-crate-metadata.json`
  file with a text editor and add the missing properties. Keep tweaking the
  metadata file until the validator reports a valid RO-Crate.
* [ADVANCED] Change the workflow language. If you used the default options for
  `rocrate add workflow` in Part 1, the `programmingLanguage` of the workflow
  will be CWL. Open `ro-crate-metadata.json` and change the language to Python,
  then run the validator again to check that the crate is still valid.
    + **📝 Tip**: you can use an internal identifier such as `#python` to
      replace `https://w3id.org/workflowhub/workflow-ro-crate#cwl`.

## Additional information

The [RO-Crate
tutorial](https://github.com/crs4/bbmri-it-school-tutorials/blob/main/07-tutorial-fair-workflows/RO_crate.md)
contains detailed information on creating and validating RO-Crates.
