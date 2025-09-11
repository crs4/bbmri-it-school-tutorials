
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
Directory.

Open [this dedicated page](./task-2.2/README.md) for complete instructions.

## Task 2.3: execute test query

Now your biobank and its collections should be fully integrated in the
Directory.  It's time to query the catalogue to see if you can find your
metadata.

Open [this dedicated page](./task-2.3/README.md) for complete instructions.


# Register with Sample Locator

Now that your biobank is integrated with Directory, it's time to connect it to
the Sample Locator.

## Task 3.1: deploy Bridgehead

First thing to do is to deploy and configure the Bridgehead on your biobank's
infrastructure.

Open [this dedicated page](./task-3.1/README.md) for complete instructions.


## Task 3.2: verify connection between Locator and Bridgehead

At this point, verify that the Sample Locator and your Bridgehead are
communicating.

Open [this dedicated page](./task-3.2/README.md) for complete instructions.


## Task 3.3: extract organization data from Directory

Now you need to implement a script to extract organization data from Directory.

Open [this dedicated page](./task-3.3/README.md) for complete instructions.


## Task 3.4: extract data from your BIMS and transform it to FHIR

Implement a script to extract data from your BIMS and transform it to FHIR,
serialized as JSON.

Open [this dedicated page](./task-3.4/README.md) for complete instructions.

## Task 3.5: import JSON FHIR into BlazeStore

At this stage, import your FHIR data into the BlazeStore, where the Bridgehead
can access it and query it.

Open [this dedicated page](./task-3.5/README.md) for complete instructions.

## Task 3.6: execute test query

Your integration should be complete and operational now, with the full ETL
process loading sample metadata into the BlazeStore and making it accessible to
the Bridgehead and thus the Sample Locator.  Let's run some queries
to see how it works.

Open [this dedicated page](./task-3.6/README.md) for complete instructions.

## Task 3.7: dealing with updates

Extend your ETL to deal with updates to your collections.

Open [this dedicated page](./task-3.7/README.md) for complete instructions.


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
