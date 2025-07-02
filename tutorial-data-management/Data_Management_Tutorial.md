# Data Management Tutorial

In this tutorial you will practice what we've learned during the lessons on

* Relational Databases
* NoSQL Databases
* Programmatic Access
* Molgenis

## Relational Databases

In this section we will perform some operations on a relational database that uses the [OMOP](https://www.ohdsi.org/data-standardization/).

We will talk about OMOP in future lessons, for now we will use it as a database with a schema and some preloaded data.

OMOP can be loaded using different DBMS. For this tutorial we will adopt [PostgreSQL](https://www.postgresql.org/) run using docker. 

### Steps

1. Clone the repository with the tutorials 

   ```bash
   $ git clone https://github.com/crs4/bbmri-it-school-tutorials.git
   ```

2. Download the file Data_Management_Tutorial/omop.zip from https://space.crs4.it/s/JzzPC2wPGFiHR7y and extract the ZIP file in the `tutorial-data-management/01-Relational-databases` directory (i.e., the directory with the PostgreSQL's docker compose file)

3. Run the compose

   ```bash
   docker compose up -d
   ```

   The compose file contains two services: 
   
   - PostgreSQL (`postgres`)
   - pgAdmin (`pgadmin`), the most common client to manage PostgreSQL

   The `postgres` service in the compose file mounts the omop.sql file in the initdb directory, so the OMOP schema will be automatically loaded.

   **NB: the schema is quite big (2.4GB) so it will take some time to load).**
   **To check when PostgreSQL is ready, use `docker-compose logs -f postgres` and wait the message "PostgreSQL init process complete; ready for start up."**

4. Access to pgAdmin web interface using a browser at the URL http://localhost:8888 and login using the credentials user: `admin@bbmri-school.it` pwd: `password`

5. Configure a new server:
   
   * Click on "Add New Server"
   * In the "General" tab, set the name bbmri-it-school-omop
   * In the "Connection" tab set the following parameters
     * Host Name/Address: postgres (**Question: Why can't we use localhost???**)
     * Port 5432
     * Maintanance database: bbmri-it-school
     * Username: postgres
     * Password: postgres
   * Click on "Save"

   You should be connected to the database loaded before. The tree on the left should look like this:

   ![OMOP Schema][./images/01-omop-schema.png]

6. This OMOP schema has only the terminology tables loaded; now we can proceed to load the data in the 
   CDM tables. There is a series of .csv files in the `tutorial-data-management/01-Relational-databases/omop_data`
   directory that contains the data to be loaded in the CDM tables. Create a python script that reads the 
   .csv files and loads the data in the corresponding tables. Notice that due to foreign key constraints you will have to follow this order;
   Hint: you can use the csv and psycopg libraries. 

     - `person`
     - `provider`
     - `visit_occurrence`
     - `visit_detail`
     - `observation`
     - `condition_occurrence`
     - `device_exposure`
     - `drug_exposure`
     - `death`

7. Once the data is loaded, open a pgadmin query tab (query tool button ) in a way to start making some queries anc creation of object in the OMOP DB, via pure SQL.
   First, let's run this aggregation query: 

   ```sql
   SELECT
     person_id,
     COUNT(*) AS observation_count
   FROM omop_cdm.observation
   GROUP BY person_id
   ORDER BY observation_count desc
   ```

   What is this query doing? 

8. Try to write the queries that answer to these business questions: 
   - Count the number of persons per gender;
   - Get all the persons that were diagnosed of a specific diagnosis type (chooose one) each year. Remember that the Condition table is the one that 
     carries the diagnosis information

9. Drop one of the indexes on the `omop_cdm.concept_ancestor` table:

  ```sql
  DROP INDEX idx_concept_ancestor_id_1
  ```

  Now execute this query: 
   
  ```sql
  SELECT * FROM omop_cdm.concept_ancestor WHERE ancestor_concept_id = 45635110
  ```

   How long does it take to execute?
   Now, recreate the index: 
    
  ```sql
  CREATE INDEX idx_concept_ancestor_id_1 ON omop_cdm.concept_ancestor(ancestor_concept_id);
  ```
  
  This will take a long time. Now, re-execute the previous query. How long does it take now?

10. Create a view namd `v_person_observation` that contains the person_id and the observation_count for each person. 
    Use the query you wrote in step 7 as a base.
    In this view, mark the count for the person '40766239'.

11. Add this log table:
      
    ```sql
    CREATE TABLE omop_cdm.log (
        id SERIAL PRIMARY KEY,
        action VARCHAR(255) NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

12. Create a trigger that logs every time a new record is inserted in the `omop_cdm.observation` table. The trigger should insert a record in the `omop_cdm.log` table with the action "insert" and the current timestamp.

13. Add a new row in the observation table: 
    
    ```sql
    INSERT INTO omop_cdm.observation(observation_id,person_id,observation_concept_id,observation_date,
							  observation_datetime,observation_type_concept_id,value_as_number,
							  value_as_string,value_as_concept_id,qualifier_concept_id,
								unit_concept_id,provider_id,visit_occurrence_id,visit_detail_id,
								observation_source_value,observation_source_concept_id,unit_source_value,
								qualifier_source_value,value_source_value,observation_event_id,
								obs_event_field_concept_id)
     values('8100','28','40766239','2025-07-01',null,'38000280',null,null,'0',0,0,49,1755,1001755,93027-1,37020580,null,null,null,null,null
    )
    ```

14. Check the log table to see if the new record has been logged.

15. Check the view to see if the count for the person '40766239' has been updated.

## NoSQL Databases

In this section we will perform some operations on a NoSQL database that uses the [MongoDB](https://www.mongodb.com/) engine.
We will run a simple mongoDB instance in a container using docker, inspect the data and perform some simple queries using the mongo shell.

### Steps

1. In a shell, go inside the `tutorial-data-management/02-NoSQL-databases/mongodb` directory and deploy and run the container:

   ```bash
   docker compose build
   ```

   Then, once that the build is completed, run the container:

   ```bash
   docker compose up -d
   ```

2. Enter to the the container, using the command:

   ```bash
   docker compose exec -it mongodb bash
   ```

2. Enter to the mongo shell, using the command:

   ```bash
   mongosh
   ```

3. Once inside the shell, chabge the database to use ours:

   ```bash
   use biobankDB
   ```

4. List the collections in the database. There should be five collections: biobanks, diseases, patients, samples, sampletypes

   ```bash
   show collections
   ```

5. List the documents in the biobanks collection:

   ```bash
   db.biobanks.find().pretty()
   ```

6. Filter the biobanks by name, e.g., to find the biobank with name "Biobanca di Ricerca Napoli":
   
   ```basg
   db.biobanks.find({name: "Biobanca di Ricerca Napoli"}).pretty()
   ```

7. Execute one of the queries examples in the queries_examples  directory(simply copy the overall code in the shell). For each query, try to understand what it is trying to do in detail, according to the operators that it is using.

8. Try to modify the "sample per year" query by adding also the sample type in the aggregation.
  
## SQLAlchemy and Alembic

In this part we will practice the creation of a database programmatically using SQL Alchemy and versioning of the database with Alembic.

We'll create a simple database based on this diagram:

```mermaid
erDiagram
    PARTICIPANTS {
        string participant_id PK
        string first_name
        string last_name
        date date_of_birth
        string gender
    }

    SAMPLES {
        string sample_id PK
        date collection_date
        string sample_type
        string participant_id FK
    }

    DIAGNOSIS {
        string diagnosis_id PK
        string condition
        date diagnosis_date
        string severity
        string participant_id FK
    }

    PARTICIPANTS ||--o{ SAMPLES : ""
    PARTICIPANTS ||--o{ DIAGNOSIS : ""
```

We will use as DBMS the same PostgreSQL instance used for the [01-Relation-databases tutorial](#relational-databases)

### Database Creation

1. First of all we need to create the directory and the [virtual environment](https://docs.python.org/3/library/venv.html) where we install the dependencies needed

   ```bash
   $ mkdir biobank_manager # Create the new directory
   $ cd biobank_manager  # Enter the directory
   $ python -m venv venv  # Create the virtual environment
   $ source venv/bin/activate  # Activate the virtual environment (from now on the python commands will use the one in the venv)
   ```

1. Now we can install the dependencies

   ```bash
   pip install sqlalchemy alembic psycopg2
   ```

1. Create the following directories and files

   ```
   biobank_manager/    # main directory
     biobank_manager/  # main python module
       __init__.py  
       conf.py         # file with configurations
       database/       # directory with the database definition
         __init__.py
         models.py     # file with the SQLAlchemy models
   ```

1. In the `conf.py` add DATABASE_URL variable using the following template. Set the values for user, password and db_name

   ```python
   "postgresql+psycopg2://{user}:{password}@localhost:5432/{db_name}"
   ```

1. In the `models.py` create three models based on the the ER Diagram
   
  > [!TIP]
  > Remember to create the Base class first. Use `biobank_manager` as schema name
  >

1. In the `__main__.py` file add the instructions to:
   - create the SQLAlchemy `engine` for the `DATABASE_URL` db
   - create the schema `DATABASE_SCHEMA_NAME`
   - create all the tables

1. Run the module 

   ```bash
   $ python -m biobank_manager
   ```

   This will run the database initialization

1. Check the database in pgAdmin4. If everything is correct you should see the schema `biobank_manager` in the `bbmri-it-school` database with the 3 tables

### Insert, query, update, delete

1. First of all we will populate the database adding some data
   
   Add to the `__main__.py` file a part that creates:

   - 100 participants 
   - for each participant a random number of samples between 1 and 10
   - for each participant a diagnosis

  > [!TIP]
  > To create random name surname you can use [names-generator](https://pypi.org/project/names-generator/) package
  >

  > [!TIP]
  > For the sample type use the following list
  > "DNA", "RNA", "BLOOD", "URINE", "FECES", "BUFFY COAT"
  > 


### Database versioning

4. Alembic
   - Create baseline
   - Change something in the DB (e.g., add column)
   - Create a revision and edit it manually
   - Add another column
   - Create automatic revision

## Molgenis

### Howto: creating a schema in Molgenis EMX2 and populating it

As we have seen in the lessons, Molgenis is a platform that allows to create and manage data models, import data, and create reports.
Schema definition and data import can be done in many ways, here we will explain how to do it with a series of
.csv files. The purpose is to create in Molgenis the same schema created in the SqlAlchemy tutorial. 
To to this, we will need some .csv files, and in particular: 
- `molgenis.csv`: contains the definition of the overall schema: tables, and for each table, fields and 
                  references/constraints 
 - .csv files for the data: these CSVs files are one for each table,and must have the same name as the table.
   For example, if we have a table named `participants`, we will have a file named `participants.csv` that contains the data for that table.
   Each .csv file must have a header with the names of the fields, followed by a row for each different record.

#### Defining the schema: the molgenis.csv file
The `molgenis.csv` file is a CSV file that contains the definition of the schema. It has the following columns:

tableName,tableExtends,columnName,label,columnType,key,required,isReadonly,description,refSchema,refTable,refBack,refLabel,defaultValue,validation,message,computed,semantics

This is the header of the file. Then, all the data following the header will be the definition of the schema. Not all columns above should be valued, let's analyze the mosrt important:

- `tableName`: the name of the table
- `columnName`: the name of the column in that table
- `label`: the label of the column, that will be used in the UI
- `columnType`: the type of the column, e.g., `string`, `integer`, `date`, `boolean`, `ref` (used for references, to other tables)

Example: to define some fieds of the "Samples" table we will have:
- Samples,,id,Identifier,int,1,,,Identifier of the sample
- Samples,,collection_date,Collection date,date,,,Date of collection of the sample,,,,,,,,,,,

For the participants: 
- Participants,,participant_id,Identifier,int,1,,Identifier of the participant,,,,,,,,,,,
- Participants,,last_name,Last Name,string,,,Last Name of the participant,,,,,,,,,,,

As Samples must also have a referenct to a participant, we will also have a column of the Samples table defining that:
- Samples,,participant,Participant,ref,,,,The participant that the sample belongs to,,Participants,

#### Adding the data: the participants.csv, samples.csv, and diagnosis.csv files
For each table defined in the `molgenis.csv` file, we will have a corresponding .csv file that contains the data for that table.
Each csv file must have a header with the names of the fields, followed by a row for each different record.
For example, the `participants.csv` file will have the following header and data (one example record only):

```csv
participant_id,last_name,first_name,date_of_birth,gender
1,Smith,John,1985-04-12,M
```

### Steps

1. From the docker compose file in the `tutorial-data-management/04-Molgenis-EMX2` directory, start Molgenis:
   ```bash
      docker compose up -d
      ```
    Then, check that the server is up and running by going to the URL http://localhost:8080 and logging in with admin/admin
2. Create a new database and name it bbmri-it-school-biobank
3. Create the molgenis.csv, participants.csv, samples.csv, and diagnosis.csv files in the `tutorial-data-management/04-Molgenis-EMX2/data` directory.
   - The `molgenis.csv` file should contain the schema definition as explained above.
   - The `participants.csv`, `samples.csv`, and `diagnosis.csv` for the data; 
   - 
4. Create the schema and import the data into molgenis. This operation can be done either via the interface, or 
   via the python client [PyClient](https://molgenis.github.io/molgenis-emx2/#/molgenis/use_usingpyclient).
   From the interface, once created the database, click on its name in the database list of the molgenis home page,
   Then click on "Up/Download" in the horizontal menu. Browse firsh the molgenis.csv file, and upload it. This will 
   create the schema. Then, do the same with the participants.csv, samples.csv, and diagnosis.csv files.
   If you want to use the python client instead, you can follow the instructions in the [PyClient documentation](https://molgenis.github.io/molgenis-emx2/#/molgenis/use_usingpyclient).


5. Navigate the UI: you can now navigate the schema, clicking on "Tables" in the horizontal bar" and then on one 
   of the tables. Notice that the interface allows you also to add additional rows in a table: try to do it!

6. Create a script with [PyClient](https://molgenis.github.io/molgenis-emx2/#/molgenis/use_usingpyclient)


