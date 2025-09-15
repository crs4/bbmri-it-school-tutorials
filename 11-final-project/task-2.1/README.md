# Task 2.1: register BB and Collections with Directory

## Your task objective

1. Register your Biobank and your Collections into the [mock
   Directory](https://directory.bbmri-school.cloud-ip.cc) deployed
   for this final project

At the end of this task you should see your biobank and its
collections in the Directory interface, with
coherent information in relation to your BIMS' data.

## Instructions

The following are the high-level steps we suggest you follow.

1. Access the test Directory instance at this URL: <http://directory.bschn.ikmx.cloud/>.
    * Log in using the credentials that you have been provided.
2. Insert into `Persons` your biobank's contact persons (at least one). They
   will be part of the metadata of your biobank and collections.
3. Identify how many collections to create for your biobank, based on the synthetic data provided for your BB.
   * You can refer to the "Possible Collections" column of the BIMS table in [Task 1.1](../task-1.1/README.md).
4. Choose the main metadata for Biobank and Collections (ID, PID, Name, Description, etc).
5. Prepare the additional metadata that is required in the Directory for your
   biobanks and collections (some of data are mandatory) -- for example:
    - Diagnosis available
    - Samples materials types
    - Dimension of the population and of the samples
    - Age range

6. Finally, insert the data into the `Biobanks` and `Collection` tables
7. Point your browser to the [Directory](http://directory.bschn.ikmx.cloud/) and
   verify for the presence of your biobank and its collections. Verify the
   coherence of all data with respect to what is contained in the BIMS.

⚠️ **Important Note** The internal codes in your BIMS are not the same used in the Directory. You will have to map
them to the appropriate ones used by the Directory.
* You can find the codes used by Directory under DirectoryOntologies / Ontology
  Tables and under DirectoryOntologies / Data Tables.  The
  relevant ones include MaterialTypes, SexTypes, DiseaseTypes.
* You can decide to implement a script that, starting from the BIMS tables
  creates the entries for the Directory, or to make partial scripts for some of the metadata.
