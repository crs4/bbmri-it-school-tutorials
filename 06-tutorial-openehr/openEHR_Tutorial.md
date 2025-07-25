# openEHR Tutorial

In this tutorial you will practice what we have learned during the lesson on openEHR. In "Solutions" you will find all the artefacts created during each major step of this tutorial and the assignments/tests solutions.

## 1. Template creation (Optional)
This optional section is intended for those who want to learn how to create a template in openEHR. If you want to skip this task, you can retrieve the final template called "biobank_report_template.opt" and the entire fileset "biobank_report_template.zip" from the "Solutions" folder. The opt will be used to upload the template in EHRBase whereas the fileset will be used to recreate the Archetype Designer project that you will eventually use to get the path needed to query each node. 

### 1.1 Information
The objective of this section is to create an openEHR Template that contains the following information:
- biobank name 
- biobank patient identifier : the unique identifier for the patient inside the biobank
- date of birth
- country of birth
- place of birth
- sex assigned at birth
- primary diagnosis
- date of diagnosis
- age at diagnosis
- sample id
- sample material type 
- sample prevervation_mode 
- year of sample collection
 

### 1.2 Mapping information to openEHR Archetypes
The information we want to persist is mapped against existing archetypes, when possible.
The final mind map model is already given to you and it is shown in the following:
![Mindmap biobank report template](./images/01-mindmap.png)

If you prefer, you can use xmind, or similar software, to open the file that have produced the image above or another version of the mind map created by the Archetype Designer from the template. Both files can be found in the directory mindmap of this tutorial under the name, respectevely, "biobank_report_template.xmind" and "biobank_report_template_from_Archetype_Designer.xmind".

The information, that we listed in the previous section, will be stored according to these mappings:

| information | nodename | original nodename | archetype | archetype name | original archetype name |
| ----------- | -------- | ----------------- | --------- | ---------------- | ------------------------ |
| biobank name | biobank name    | name | openEHR-EHR-CLUSTER.organisation.v1  | Biobank | Organisation |
| biobank patient identifier |  biobank patient identifier | Case identifier | openEHR-EHR-CLUSTER.case_identification.v0 | Patient identification | Case identification | 
| date of birth | Date of birth | Date/time of birth (DOB) | openEHR-EHR-EVALUATION.birth_summary.v1 | Birth summary | Birth summary |
| country of birth | Country of birth | Country of birth | openEHR-EHR-EVALUATION.birth_summary.v1 | Birth summary | Birth summary |
| place of birth | Place of birth | Place of birth | openEHR-EHR-EVALUATION.birth_summary.v1 | Birth summary | Birth summary |
| sex assigned at birth | Sex assigned at birth | Sex assigned at birth | openEHR-EHR-EVALUATION.gender.v1 | Gender | Gender |
| primary diagnosis | Primary diagnosis | Problem/Diagnosis name | openEHR-EHR-EVALUATION.problem_diagnosis.v1 | Diagnosis | Problem/Diagnosis |
| date of diagnosis | Date of diagnosis | Date/time of onset | openEHR-EHR-EVALUATION.problem_diagnosis.v1 | Diagnosis | Problem/Diagnosis |
| age at diagnosis | Age at diagnosis | Time offset | openEHR-EHR-CLUSTER.timing_nondaily.v1 | Timing | Timing Nondaily |
| sample id | Sample ID | Stored specimen ID | openEHR-EHR-EVALUATION.specimen_summary.v1 | Specimen summary | Specimen summary |
| sample preservation mode | Sample preservation mode | Specimen storage| openEHR-EHR-EVALUATION.specimen_summary.v1 | Specimen summary | Specimen summary | 
| sample material type | Sample material type | Specimen type | openEHR-EHR-CLUSTER.specimen.v1 | Specimen | Specimen |
| year of sample collection | Year of sample collection | Collection date/time | openEHR-EHR-CLUSTER.specimen.v1 | Specimen | Specimen |



### 1.3 Retrieving Archetypes from CKM
Open the ckm address https://ckm.openehr.org/ckm in a browser. First, we look for the archetype  openEHR-EHR-COMPOSITION.report.v1

1. Select "Archetypes" if needed (already selected at start) and in the blank space search for "report". See figure below

![TODO](./images/02-ckm-search.png)

2. double click "Report(v1)"" under "Composition" section. On the right will appear the data for the report composition openEHR-EHR-COMPOSITION.report.v1 that we will use as template container. 

3. check that at the tab "Attribution" there is written: 
Archetype ID  [the archetype you are looking for (i.e.,openEHR-EHR-COMPOSITION.report.v1 )]

4. export the archetype in adl format. see figure below

![Archetype Export](./images/03-ckm-export.png)

5. Now repeat the steps 1-4 for the following archetypes:

| archetype | search for | double click | 
| ----------------------  | ----------  | --------------  |
| openEHR-EHR-CLUSTER.organisation.v1 | organisation | Cluster->Organisation(v1) |
| openEHR-EHR-CLUSTER.case_identification.v0 | identification | Cluster->Case Identification(v0) |
| 	
openEHR-EHR-SECTION.adhoc.v1 | adhoc | Section->Adhoc(v1) |
| openEHR-EHR-EVALUATION.birth_summary.v1 | birth | Entry->Evaluation->Birth_Summary(v1) |
| openEHR-EHR-EVALUATION.gender.v1 | gender | Entry->Evaluation->Gender(v1) |
| openEHR-EHR-EVALUATION.problem_diagnosis.v1 | diagnosis | Entry->Evaluation->Problem_Diagnosis(v1) |  
| openEHR-EHR-CLUSTER.timing_nondaily.v1 | timing | Cluster->Timing_Nondaily(v1) |
| openEHR-EHR-EVALUATION.specimen_summary.v1 | specimen | Entry->Evaluation->Specimen_Summary(v1) |
| openEHR-EHR-CLUSTER.specimen.v1 | specimen | Cluster->Specimen(v1) |

### 1.4 Creating the template in Archetype Designer
1. open the Archetype Designer https://tools.openehr.org/designer/ and log in via github, Google or Microsoft account. 

2. create a new project

3. enter the project

4. import all the archetypes. Click "import" button, on top of the page, then "Browse" and choose all the previously downloaded archetypes, then "upload all", and at last push the "close" button.

5. Click "New->Template". In the pop up window choose openEHR-EHR-COMPOSITION.report.v1 as the root archetype id and call this new template "biobank_report_template"

6. click "extension" of other_context and add the Organisation archetype that you find on the bottom right of the page

7. click "additional_details" and add case_identification

8. click "content" and add openEHR-EHR-SECTION.adhoc.v1 which you rename "Demographics" by clicking twice the old name and typing the new one.

9. click "items" and add the following items:
    - birth_summary
    - gender

10. click "content" and add openEHR-EHR-SECTION.adhoc.v1 which you rename "Diagnosis" by clicking twice the old name and typing the new one.

11. click "items" and add the following item:
    - problem_diagnosis
    
12. click "specific_details" and add "timing_nondaily"

13. click "content" and add openEHR-EHR-SECTION.adhoc.v1 which you rename "Sample" by clicking twice the old name and typing the new one.

14. add "specimen_summary" to "items"

15. add "specimen" to the "additional_details" section of "specimen_summary"

16. rename all the nodes and archetypes that contain the information we are interested in accord with each row of the table reported in section 1.1. That is, find the node original name and change it to the new node name and, if needed, change the corresponding archetype name to the new one.

17. remove all nodes not mapped to one of the data we want to store. Click the node you need to remove, e.g, Report ID under context->other_context, on the right change the occurrences from 0..1 or 0..* or any other value to 0..0. The first number is the minimum of occurrences, the second one is the maximum, so we are setting to zero the minimum and maximum occurences for each node we are not interest in.
The final template should look like this:
![Template Only Selected Nodes](./images/04-template-only-selected-nodes.png)


18. set the occurrences for the Samples. Click "Specimen summary" and set the occurrences to "0..*" . Asterisk means any number so now we can attribute any number of samples, include none, to each patient.

19. click "year of sample collection". On the right remove "Interval:Date Time" from available types and set Pattern dropdown menu to "year only".

20. click Save, fill it with the needed version info (your choice), then click "export" and then "export->export to OPT"

## 2. Upload Template into EHRBase 
In this section we set up EHRBase and interact with it. The final objectives are the insertion of the template just created and the retrieval of an example composition for that template.


### 2.1 Start EHRBase
 Run the compose

   ```bash
   docker compose up -d
   ```

   The compose file contains two services: 
   
   - ehrbase : default user credentials ehrbase-user/SuperSecretPassword
               default admin credentials ehrbase-admin/EvenMoreSecretPassword

   - ehrdb : postgres db for ehrbase

   Check that ehrbase is up with this command:
   ```
   curl -i "http://localhost:8080/ehrbase/rest/status" -H "Authorization:Basic ZWhyYmFzZS11c2VyOlN1cGVyU2VjcmV0UGFzc3dvcmQ=" -H "Content-Type: application/json"  
   ```
   The response should be something like this:
```
HTTP/1.1 200 
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Type: application/xml
Transfer-Encoding: chunked
Date: Tue, 22 Jul 2025 09:47:16 GMT

<?xml version='1.0' encoding='UTF-8'?><status><ehrbase_version>2.15.0</ehrbase_version><openehr_sdk_version>2.21.0</openehr_sdk_version><archie_version>3.12.0</archie_version><jvm_version>Eclipse Adoptium 21.0.6+7-LTS</jvm_version><os_version>Linux amd64 5.15.0-139-generic</os_version><postgres_version>PostgreSQL 16.2 on x86_64-pc-linux-musl, compiled by gcc (Alpine 13.2.1_git20231014) 13.2.1 20231014, 64-bit</postgres_version></status>
```

### 2.2. Interact with EHRBase

EHRBase exposes a REST API so you can use any REST client of your choice to interact with it. For instance, you can use Postman, a standalone app, or curl, that runs from the command line as you have seen before, or even your own code in any language you like. In this tutorial we will use openEHRTool, a frontend app developed here at CRS4 specifically for EHRBase. 

#### 2.2.1 Steps via openEHRTool

**Install openEHRTool**

Clone the repository for the latest, asynchronous, version of the tool, still in development:
```
git clone https://github.com/sasurfer/openEHRTool-v2.git
```
Follow the instructions in README.md for the Docker "Separated" installation and know how to log in.

If you have issues please report them via github. 

**NOTE** If you prefer a stable version you can use the first version of the openEHRTool, which is still synchronous so definitely slower. It can be cloned with:
```
git clone https://github.com/crs4/openEHR-tool.git
```
As before, follow the steps described in README.md for the Docker "Separated" installation.

**Upload the template**

Click the tree-like figure on the left, then "insert template". Pick the file "biobank_report_template.opt" after clicking "Browse" and then hit the "Submit" button.
![Insert Template](./images/05-insert-template.png)

It is expected this message in return:
```
{
  "template_id": "biobank_report_template",
  "status": "success"
}
```
Now, if you click "List Templates" and "Submit" you should see some info on the newly created template.

**Note** If you make some changes to the template, you can upload it over the old one. This behaviour is set in properties contained in .env.ehrbase configuration:
```
SYSTEM_ALLOW_TEMPLATE_OVERWRITE=true
EHRBASE_TEMPLATE_ALLOW_OVERWRITE=true
```

**Create an example composition**

Go to the composition methods, the icon is a pen that writes on paper. Click on "Retrieve Example Composition", select the template just inserted leaving flat format and click "Submit". The composition can be saved with the button "Save results to file". Save the file as composition.json as suggested.

Now we can edit the composition and remove the rows that contain some optional nodes that EHRBase create for us. In particular we can remove the rows for all the nodes that have "_work_flow_id" or "_guideline_id" in their path. In addition, the following nodes along with their assigned value can be removed as well:
- "biobank_report_template/context/_end_time"
- "biobank_report_template/context/_health_care_facility|name"

Name the new file "composition_modified.json"

**Note** year of sample collection is saved as a datetime object because EHRBase do not understand yet "year only" format so we will save is as year-01-01T00:00:00

## 3. Create the compositions
IN this section we create the compositions from syntetic data. In particular, the file "patients_data.json" contains the fictitious data for 50 patients distributed among three biobanks. 

- Write a script that read patients_data.json and create a composition for each patients using as a model the composition_modified saved before.

**Note 1** Age at diagnosis is expressed according to ISO8601 that is:
P[n]Y[n]M[n]DT[n]H[n]M[n]S
P = period designator (starts the duration), Y = years, M = months, D = days, T = time separator (indicates time part follows), H = hours, M = minutes, S = seconds. So, for age in years: PnY e.g.,P20Y

**Note 2**  In "biobank_report_template/sample/specimen_summary:0/ 0 is the occurence so for the first sample you have to use 0 for the second 1 and so on.

**Note 3** In "Solutions" you find "create_data_for_compositions.py" which is the Python code used to create "patients_data.json". Feel free to play with it. Just remember that the query solutions will vary if you change "patients_data.json".

## 4. Upload the compositions into EHRBase

Firstly, we upload only the first compositions so we see the procedure then we make use of a feature of openEHRTool that makes it possible to upload a batch of compositions.

So the steps in openEHRTool are:
1. create an EHR. Click the folder like symbol, choose "Post" type of methods and select "Create EHR with/without EHRid specified". Leave the EHRid blank and click "submit". An EHR will be created, that is the container for patient files, i.e.,compositions. Copy the EHRid on the clipboard.


2. post the first composition. Click the composition symbol (it looks like a pen on paper) and choose "Post" type of methods and "Insert Composition" method. Paste the EHRid you copied earlier (If you do not have it click, on the right edge of the browser window, the folder icon, there you will find all the EHRs you created). Select the template, leave "flat" format and browse the file then push the "Submit" button. The response will contain the id of the composition inserted into the server.

3. in order to post the remaining 49 compositions and avoid creating one by one the EHR and posting the composition click the composition icon, choose "Post" methods type and select the method called "Batch insert compositions different EHRid". Inside the method, select the template, leave "flat" format and yes to "create EHR on the fly" then browse the 49 files and click "Submit". The response will be a list of compositions id and EHRid like this:
```
{
  "status": "success",
  "compositionids": [
    "ed6482c1-8b63-44ff-abd4-5d6ddf5e8da4",
    "9c93c9b6-5d51-49b7-a8a7-31c242828b57",
    ...
    "17992bba-3f70-46b0-a063-abf4cb93bc71"
  ],
  "ehrids": [
    "3ca995bb-26e1-40dc-a5e3-b471cbe73339",
    "c6ac56d9-0559-48dc-8b60-a5e931a5b4d0",
    ...
    "27e5867a-bf67-4103-9826-5471eef68d60"
  ]
}
```

## 5. Query the compositions
In order to query the compositions we suggest two possible ways:
-continue to use openEHRTool. Section 5.1
-set up and use aqlbetter. Section 5.2
Section 5.3 contains the tests that you can carry on with either of those tools.

**Note** aqlbetter is an adaptation for EHRBase of AQL Builder, a software written by Better to help in writing queries for their own platform and released open-source. The original software information can be found at [aql builder site]( https://docs.better.care/studio/aql-builder/overview ).

## 5.1 Continue to use openEHRTool
If you created the template according to chapter 1 skip to the subsection 5.1.2.

### 5.1.1 Set up Archetype Designer

1. open the Archetype Designer https://tools.openehr.org/designer/ and log in via github, Google or Microsoft account. 

2. create a new project

3. enter the project

4. import the fileset. Click "import" button, on top of the page, then "Browse" and choose "biobank_report_template.zip", then "upload all", and at last push the "close" button.

5. click on the template. It will be useful to get the paths needed in the queries


### 5.1.2 Query the compositions

To run a query follow these steps:
1. click the icon with the magnifying glass and the paper 
2. click "Run query" method. 
3. type your query in the "AQL Query" box
4. optionally use additional filters: fetch (equivalent to SQL LIMIT), offset, and query parameters
5. the GET and POST methods are available. Use POST when you have a long query that does not fit into the Browsers URL limit or you are sending sensitive data in the query, otherwise GET and POST are equivalent. 
6. click the "Submit" button. Optionally there are boxes for the additional filters: fetch (equivalent to SQL LIMIT), offset, and query parameters.

**Note 1** The path for each node can be retrieved from the Archetype Designer in Details->Resolved Path. You can use absolute paths that start from the composition root or relative paths, that are relative to an element inside the path. 
```e.g. year of sample collection
Absolute Path
c/content[openEHR-EHR-SECTION.adhoc.v1, 'Sample']/items[openEHR-EHR-EVALUATION.specimen_summary.v1]/data[at0001]/items[openEHR-EHR-CLUSTER.specimen.v1]/items[at0015, 'year of sample collection'] 
where c is the composition symbol in the query, Relative path 
s/items[at0015, 'year of sample collection'] 
where s is the specimen cluster symbol in the query.
```

**Note 2** Remember to add for a node "/value/value" and "/value" to each path found respectevely in Archetype Designer and in aqlbetter. For instance "year of sample collection" in Archetype Designer has a path:
```
/content[openEHR-EHR-SECTION.adhoc.v1, 'Sample']/items[openEHR-EHR-EVALUATION.specimen_summary.v1]/data[at0001]/items[openEHR-EHR-CLUSTER.specimen.v1]/items[at0015, 'year of sample collection']
```
while in aqlbetter has a path:
```
/content[openEHR-EHR-SECTION.adhoc.v1 and name/value='Sample']/items[openEHR-EHR-EVALUATION.specimen_summary.v1]/data[at0001]/items[openEHR-EHR-CLUSTER.specimen.v1]/items[at0015 and name/value='year of sample collection']/value
```
The correct path if we want the value of the node is:
```
/content[openEHR-EHR-SECTION.adhoc.v1, 'Sample']/items[openEHR-EHR-EVALUATION.specimen_summary.v1]/data[at0001]/items[openEHR-EHR-CLUSTER.specimen.v1]/items[at0015, 'year of sample collection']/value/value
```
This is what we find at the path shown by Archetype Designer without our addition:
```
{
        "_type": "ELEMENT",
        "name": {
          "_type": "DV_TEXT",
          "value": "year of sample collection"
        },
        "value": {
          "_type": "DV_DATE_TIME",
          "value": "2017-01-01T00:00:00"
        },
        "archetype_node_id": "at0015"
}
```
and at the path shown by aqlbetter without our addition (that is also at the path shown by Archetype Designer with an addition of only one "value") :
```
{
        "_type": "DV_DATE_TIME",
        "value": "2021-01-01T00:00:00"
}
```
Finally with another "value" added:
```
"2021-01-01T00:00:00"
```

## 5.2 Set up aqlbetter
Clone the aqlbetter-dockerized github repository:
```
git clone https://github.com/crs4/aqlbetter-dockerized.git
```
Follow the instructions to run the dockerized version of the software. Once the container is running, go to http://localhost and type a valid username,password for EHRBase. You will be redirected to a second page where you type the query on the right box, run it with the play button and see the results on the page bottom. The lefthand side of the page allow to see the template and get the path, needed for queries.

## 5.3 Test your querying skill

Create a query for each of the following questions:
1. Create a table of composition_id,ehr_id for all the compositions that are stored for the template 'biobank_report_template'.

2. Count the compositions that have 'biobank_report_template' as template_id.
    
3. Retrieve all the compositions for a patient given the ehr_id.

4. Retrieve the unique biobank name values.

5. Find how many patients are stored in each biobank (hint: use multiple queries. Use results of previous query and create a parametric query with parameter biobank_name).

6. Find how many patients have the 'Colorectal Cancer' as Primary diagnosis

7. Find how many female patients have the 'Colorectal Cancer' as Primary diagnosis in the biobank "FirstBiobank".

8. Retrieve the composition_id and sex assigned at birth for the patients in the biobank "ThirdBiobank" ordered by gender.

9. The same query as 8 but now show only the results from second to fifth.

10. Retrieve the sample id, ehr_id, year of sample collection for all the samples collected between 2010-01-01 and 2012-02-01 

