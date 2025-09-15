# Task 3.2

## Your task objective

In this task, starting from your BIMS data, you will generate the 
FHIR resources instances to be loaded into your bridgehead. 
At the end of the task you will have a set of JSON files, containing all the 
FHIR resources instances related to your BIMS, Biobank and Collection data, to be 
loaded into the bridgehead in the next task.

## Instructions

The FHIR resources to be created follow the structure defined by the 
BBMRI.de/GBA Implementation guide: 

https://samply.github.io/bbmri-fhir-ig/overview.html

We will create instances for the following resources: 

 - Organization (1 for the Biobank, 1 for each collection you 
   added yesterday in the Directory)
 - Patient (1 for each donor you have in your BIMS data)
 - Specimen (1 for each sample you have in your BIMS data)

Notice that the Organization resource related to the collections has 
a reference to the Biobank Organization resource and the Specimen resource 
has a reference to the Collection resource and to the Patient resource.

You will have to generate the resources saving them in JSON files that we will
upload to the bridgehead in the next task.

## Important notes

You can generate the FHIR ressources in the way you prefer. We will 
provide some details about a python framework we developed to 
read and convert data about biomedical samples into formats compatible with the 
Federated Platform (in this case FHIR resources): 

https://github.com/crs4/bbmri-fp-etl

In order to use the framework to generate FHIR respurces, you will have to define 
a new source class that extends the AbstractSource class and implenents the 
methods to get the data and create a series of Pydantic objects that will be 
automatically converted by the framework into FHIR resources.

The pydantic objects to create are: 

- Biobank and collecions, that have to be stored into a list od objects, 
      that we can name "organizations"

- Case, that is composed by: 
    - a  Donor object
    - a  List of Sample objects

The Case object will be stored into a list of objects, that we can name "cases"

You can refer to the bbmri-fp-etl/models.py module to see the complete structure of
the pydantic objects.

Then, you will define the abstract class and implement the methods to read your 
input data. Below you can find an example of the class structure: 

```python
   from bbmri_fp_etl.sources import AbstractSource
   from bbmri_fp_etl.models import Biobank, Collection, Donor, Sample, Case
   class YourBIMSSource(AbstractSource):
         def __init__(self, ...):
              # your code here
    
         def get_biobanks_data(self):
           organizations = []
           for b in your_biobank_data:
              biobank = Biobank( ... ) # create the biobank object
              organizations.append(biobank)
              for c in your_collections_data:
                 collection = Collection( ... ) # create the collection object
                 organizations.append(collection)
           return organizations

         def get_cases_data(self):
              cases = []
              for d in your_donors_data:
                  donor = Donor( ... ) # create the donor object
                  samples = []
                  for s in your_samples_data:
                     sample = Sample( ... ) # create the sample object
                     samples.append(sample)
                     case = Case(donor=donor, samples=samples)
                     cases.append(case)
              return cases

```
Then, in yout main module you will instantiate your data source class and use the 
Converter class of the framework to generate the FHIR resources and save them into JSON files:
```python
   from bbmri_fp_etl.converter import Converter
   from bbmri_fp_etl.destinations import FHIRDest
   from bbmri_fp_etl.serializer import JsonFile
   
   if __name__ == "__main__":
         source = YourBIMSSource( ... ) # instantiate your data source
         fhir_cases_resources = FHIRDest(JsonFile('./fhir_output_cases'))
         fhir_orgs_resources = FHIRDest(JsonFile('./fhir__output_resources'))#
         converter_orgs = Converter(source, fhir_orgs_resources, Converter.ORGANIZATION)
         converter_orgs.run()
         converter_cases = Converter(source, fhir_cases_resources, Converter.CASE)
         converter_cases.run()
```

Run the main module and the framework will generate all the JSON files related
to the resources, in the two output directories you specified.


