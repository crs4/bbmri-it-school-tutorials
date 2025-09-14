# Task 1.2

## Your task objective

Register your Biobank and your Collections into the BBMRI.it School test Directory.
At the end of this task you should see your biobank and its collections in the Directory interface, with 
coherent information in relation to your BIMS' data.

## Instructions

Starting from your BIMS data, you will have to register your biobank and its collections into the test Directory.
These are some steps you could follow:

1. Access the test Directory instance at this URL: http://directory.bschn.ikmx.cloud/(credentials will be provided during the training)
2. Insert into Persons your biobank's contact persons (at least one). They will be part of the metadata of your biobank and collections.
3. Identify how many collections to create for your biobank, based on the BIMS you picked. 
   You can refer to the "Possible Collections" column of the BIMS table in Task 1.1's README.
5. Choose main metadata for Biobank and Collections (ID, PID, Name, Description, etc)  
4. Prepare some of the additional metadata that are needed  for biobanks and collections in the Directory (some of them are mandatory), as for example:

    - Diagnosis available 
    - Samples materials types 
    - Dimension of the population and of the samples 
    - Age range 
   
5. Finally, insert the data into the Biobanks and Collection tables 
6. Load the Directory interface and check for the presence of your biobank and its collections. Check for the coherence of all data in relation to what is contained in the BIMS.
   

## Important notes
⚠️ **Note** The internal codes in your BIMS are not the same used in the Directory. You will have to map 
them to the appropriate ones. You can decide to implement a script that, starting from the BIMS tables 
creates the entries fpr the Directory, or to make partial scripts for some of the metadata.
Refer to the Ontology tables in the Directory to check with ontologies are used for the various metadata.
    
   