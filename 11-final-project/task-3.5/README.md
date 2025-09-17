# Task 3.5: Enrich your bridgehead with consent information

## Your task objective
Load into the bridgehead some Consent resources that provide information about
the consents tou added to your BIMS in the task 1.2
The objective is to see the Consent resources loaded in the Bridgehead FHIR server,
and perform a CQL query to retrieve Samples/Donor according to a specific consent.

# Instructions
The Consent Resource we will create follows the specifications provided by the
Pilot project of BBMRI.it we talked about in the lectures. This is the reference
of the profiled consent resorce:

https://guide.bschn.ikmx.cloud/StructureDefinition-Consent.html

The consent resource has some metadata, a head provision of class_Specimen,
indicating that by default all is denied for the specimen, and a series of
child provisions specifying the consent conditions and the related decision.

You can find a sample Consent resource in the file Consent-example.json.

This template contains some variables into brackets that are use to identify
the information you will have to set for each Consent resource you wull create,
starting from your BIMS data.

There are some header information to set:

- UNIQUE_UUID: to be set with a unique UUID
- CONSENT_ID: unique identifier of the consent. We have a unique consent
  FHIR instance that carries all the consents of a patients for one or more CCE
  and for one or more samples. Could be set ad CONSENT-<PATIENT_ID>
- PATIENT_ID: the identifier of the patient (person) that provided the consent,
  as it matches in the related Patient resource (ref)
- ORGANIZATION_ID: the identifier of the Biobank responsible for the consent,
  as it matches in the related Organization resource (ref)

Then, for each provision.provision block, there are some detail information to set:

- CCE_ID: the identifier of the consent condition (cce_id) the provision is related to
- DECISION_ID: the decision (permit/deny) the participant made for that CCE
- SPECIMEN_ID: the identifier of the specimen (sample) the provision is related to, as it
    matches in the related Specimen resource (ref)

Notice that this block:
```
       {
                  "reference": {
                    "reference": "Specimen/[SPECIMEN_ID]",
                    "display": "Specimen/[SPECIMEN_ID]"
                  },
                  "meaning": "instance"
                }
```

Could be repeated, as there could be obe or more specimens related to the same CCE

In the same way, all the provision.provision block could be repeated for each CCE.

Finally, save all the Json files you create in a directory, and load the resources into
the Bridgehead using the blazectl tool, as you did in the previous task.

Now, we can try to perform a CQL query to retrieve Samples/Donor 
according to one or more CCEs. 

First, from your Bridgehead VM, you have to checkout the CQL query repository from GitHub :

```bash
git clone https://github.com/crs4/consent-cql-client
```
Edit some parameters in the search_specimens_by_consent.py script:

```python

FHIR_BASE_URL = "http://[BH_ADDRESS]:[BH_PORT]/fhir"
CQL_QUERY_CONTEXT = "[YOUR_PREFERRED_CONTEXT]"  # This can be Specimen or  Patient
CQL_QUERY_GRANULARITY = Granularity.[YOUR PREFERRED GRANULARITY]  # it can be count or resources
CCEs = [[YOUR_CCE_MATCHING_CODEs]]
```

In particular: 

- CQL_QUERY_CONTEXT: it is the main contexc of the CQL query. If set to "Specimen", you will
  count/get the Specimen resources that match the CCEs you provide. If set to "Patient", you will
  count/get the Patient resources that match the CCEs you provide.
- CQL_QUERY_GRANULARITY: it can be set to "count" or "resources". If set to "count", the script
  will return the number of resources that match the CCEs you provide. If set to "resources", the script
  will return the resources that match the CCEs you provide.
- CCEs: it is a list of CCE codes you want to match. You can provide one or more CCE codes.
  The CCE codes are the same you used in the Consent resources you created.

Once you hace set the parameters, you can run the script:

```bash
python3 search_specimens_by_consent.py
```

Check for the results, that should match your expectations, according to the consents you added to your BIMS.
Change the parameters and run the script again to see different results. 


