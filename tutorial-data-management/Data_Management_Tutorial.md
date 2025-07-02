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
     * Host Name/Address: postgres (Question: Why not localhost???)
     * Port 5432
     * Maintanance database: bbmri-it-school
     * Username: postgres
     * Password: postgres
   * Click on "Save"

   You should be connected to the database loaded before. The tree on the left should look like this:

   ![OMOP Schema][./images/01-omop-schema.png]


## NoSQL Databases

**NB: should we add a tutorial for this?**

## SQLAlchemy and alembic

**TBD: add a tutorial that creates the Biobank DB using SQLAlchemy and creates migration with Alambic**
### Steps

1. create the project

2. Add two models Donor and Samples

3. Create a script insert, query, update and delete

4. Alambic
   - Create baseline
   - Change something in the DB (e.g., add column)
   - Create a revision and edit it manually
   - Add another column
   - Create automatic revision

## Molgenis

**TBD: add a tutorial to create the same DB**

### Steps

1. Rub molgenis with the provided compose

2. Create the usal DB with donor and sample

3. Import data

4. Navigate the UI

5. Create a report using SQL

6. Create a script with [PyClient](https://molgenis.github.io/molgenis-emx2/#/molgenis/use_usingpyclient)


