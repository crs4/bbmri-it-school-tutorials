
# BBMRI IT School: Final Project

This final course project will give you the opportunity to **integrate your own
(toy) biobank** into a mock BBMRI-ERIC Federated Platform (FP).

The project is broken down into a set of tasks, which you must complete in
sequence.  In each task, there may be solutions suggested, but you should feel
free to do things your own way -- so long as you can achieve the objectives.

# Setup

## Task 0: setup

First thing: connect to the laboratory setup.

Open [this dedicated page](./task-0.0/README.md) for complete instructions.


# Create your biobank

## Task 1.1: create your biobank

It's time to create your biobank.  Open [this dedicated
page](./task-1.1/README.md) for complete instructions.

## Task 1.2: extend biobank schema
Extend your biobank's schema to include consent and load consent data.

Open [this dedicated page](./task-1.2/README.md) for complete instructions.

# Register with Directory

## Task 2.1: register biobank and collections into Directory

Register your biobank and its collections into the Directory.

Open [this dedicated page](./task-2.1/README.md) for complete instructions.

## Task 2.2: create the Fact Table

Create the Fact Table for your collections and have them imported into the
Directory. Then, query the catalogue to see if you can find your
metadata.

Open [this dedicated page](./task-2.2/README.md) for complete instructions.


# Register with Sample Locator

Now that your biobank is integrated with Directory, it's time to connect it to
the Sample Locator.

## Task 3.1: set up Bridgehead

First thing to do is to deploy and configure the Bridgehead on your biobank's
infrastructure.

Open [this dedicated page](./task-3.1/README.md) for complete instructions.


## Task 3.2: Generate FHIR resources for the Bridgehead

Open [this dedicated page](./task-3.2/README.md) for complete instructions.


## Task 3.3: Load FHIR resources into the Bridgehead

Open [this dedicated page](./task-3.3/README.md) for complete instructions.


## Task 3.4: Query the Locator

Open [this dedicated page](./task-3.4/README.md) for complete instructions.

## Task 3.5: add support for updates

Make your ETL process idempotent and extend it to deal with updates to your collections.

Open [this dedicated page](./task-3.5/README.md) for complete instructions.


# Automation

So far you have implemented your integration as plain scripts.  work on making
it more portable and automated.

## Task 4.1: docker container images

Package your integration scripts as Docker images.

Open [this dedicated page](./task-4.1/README.md) for complete instructions.

## Task 4.2: automated execution

Implement a solution to orchestrate and automatically execute the various steps
of your ETL.

Open [this dedicated page](./task-4.2/README.md) for complete instructions.

## Task 4.3: sophisticated automated execution

Replicate in Airflow the automation from the previous task.

Open [this dedicated page](./task-4.3/README.md) for complete instructions.

## Task 4.4: create a Workflow RO-Crate for your ETL workflow

Create and validate a Workflow RO-Crate for your ETL workflow.

Open [this dedicated page](./task-4.4/README.md) for complete instructions.


# Appendix

* [Link to
slides](https://docs.google.com/presentation/d/140Ijod9uOZ2uUqe6I6Vpr1sX4ufgk8eOsEcF3IJtbn8/)
* [Link to list of biobanks](https://bbmri-it-school.crs4.it/mod/page/view.php?id=60)
