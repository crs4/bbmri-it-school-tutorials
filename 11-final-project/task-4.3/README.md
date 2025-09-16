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

### Start Airflow
On the VM, run:
```bash
  cd ~/airflow
  docker compose up -d
```

Access the Airflow web interface with your browser at http://<your VM
address>:8888

### Install the Airflow Python module

In the VM, create a virtualenv and install the `airflow` Python module.  This will allow
you to validate your workflow definition before passing it to the server.

```python
mkvirtualenv airflow
pip install "apache-airflow[celery]==3.0.6" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.9.txt"
```
Now your should have the `airflow` venv active, so your prompt should start with
`(airflow)` -- e.g.,

```bash
(airflow) [ubuntu@aws-1-2-3-4 airflow]
```

### Define a DAG

Workflows in Airflow are called DAGs -- i.e., Directed Acyclic Graphs.

Define your own DAG to run your ETL script.  Start from the example DAG provided in the [this example](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html#example-pipeline-definition).  Define the DAG to call your ETL script as a Bash command, through the BashOperator (Airflow includes a [wide variety of Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html), including many provided by the wider community).  Take inspiration from the code below.

```python
import textwrap
from datetime import datetime, timedelta

# Operators; we need this to operate!
from airflow.providers.standard.operators.bash import BashOperator

# The DAG object; we'll need this to instantiate a DAG
from airflow.sdk import DAG
with DAG(
    "etl",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="My ETL DAG",
    schedule="@daily",
    catchup=False,
    tags=["etl"],
) as dag:

    # t1 is a task created by instantiating an operator
    t1 = BashOperator(
        task_id="run_ETL",
        bash_command="<your ETL command>",
    )

```

### Write your file to the dags directory

Write your DAG file to `~/airflow/dags/etl.py`.  Airflow should detected
automatically after a few minutes.

* Open the Airflow web interface with your browser.
* On the left, select `Dags`
* At the top of the page, where it says "Search Dags", enter `etl`.  Your
workflow should show up.
* Select its name.  You should be able to see some information.  At the top
right there's a button "**Trigger**".  Press it, select "Single Run", then
"Trigger" again to run your workflow.

You should be able to monitor your workflow's execution from the Airflow web
interface.


Notice the "Schedule" information; it should say `0 0 * * *`.  That's cron
syntax for "every day at midnight", and is caused by the `@daily` schedule
inserted in the DAG specification (see above).

### Shut down Airflow
```
  cd ~/airflow
  docker compose down --volumes --remove-orphans
```
