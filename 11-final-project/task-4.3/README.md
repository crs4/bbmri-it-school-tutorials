# Task 4.3: Sophisticated automated execution

## Your task objective

1. Replicate in Airflow the automation from the previous task 4.2. I.e.,
    *  Automate the execution of your ETL process;
    *  Implement a strategy to handle errors (e.g., re-run and/or notify
       administrator);
    *  Implement a notification mechanism to notify someone when the ETL has completed (be it successfully or not).


## Instructions

The systemd automation solution you implemented previously is simple.  However,
it lacks modularity, integrated error management, notification, monitoring.
This level of functionality become important as the ETL complexity increases.

Use what you learned in the [FAIR workflows tutorial](https://github.com/crs4/bbmri-it-school-tutorials/tree/main/07-tutorial-fair-workflows) to create a simple automation with Airflow.


#### Additional information
* Airflow is installed on your BB's VM.  Activate by following these steps.
    1. Go into the `~/airflow` directory.
    2. Edit the docker compose to expose its web interface on port 8888: `sed -i -e 's/\<8080\>/8888/g' docker-compose.yaml`.
    3. Run `docker compose up -d`.
    4. You'll be able to access the dashboard at `http://localhost:8888`.
