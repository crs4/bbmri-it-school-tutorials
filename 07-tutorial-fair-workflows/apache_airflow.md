# Apache Airflow Workflows Tutorial

## Introduction to Apache Airflow

Apache Airflow is an open-source platform for creating, scheduling, and monitoring workflows programmatically. Developed by Airbnb in 2014 and later donated to the Apache Software Foundation, Airflow allows you to define workflows as code using Python, making them more maintainable, versionable, and dynamic.

### Key Features

- **Dynamic**: Workflows are defined as Python code, enabling dynamic pipeline generation
- **Extensible**: Easily define your operators, executors, and extend the library
- **Elegant**: Pipelines are lean and explicit with powerful operators and macros
- **Scalable**: Modular architecture and message queue to orchestrate an arbitrary number of workers

### Airflow vs Galaxy

| Feature | Airflow | Galaxy |
|---------|---------|--------|
| Interface | Code-based (Python) | GUI-based |
| Target users | Developers, data engineers | Scientists, researchers (no coding required) |
| Flexibility | Highly customizable with Python | Limited to tools in Galaxy toolshed |
| Version control | Native Git integration | Workflow sharing but not native Git |
| Learning curve | Steeper (requires coding) | Gentler (GUI-driven) |
| Deployment | Self-hosted or cloud | Self-hosted or cloud |

## Airflow Architecture

Airflow follows a modular architecture with several key components:

- **Webserver**: The UI to inspect, trigger, and debug DAGs and tasks
- **Scheduler**: Responsible for scheduling workflows
- **Executor**: Defines how tasks are executed
- **Metadata Database**: Stores state information

For a comprehensive understanding of the architecture, refer to the [official documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html).

## Installing Airflow

You have two main options for installing Airflow:

### Option 1: Install with pip in a virtual environment

```bash
# Create a virtual environment
python -m venv airflow-venv

# Activate the virtual environment
source airflow-venv/bin/activate  # Unix/MacOS
# or
.\airflow-venv\Scripts\activate    # Windows

# Install Airflow (constrain to a specific version for stability)
AIRFLOW_VERSION=2.7.3
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

For detailed installation instructions, refer to the [official documentation](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html).

### Option 2: Deploy with Docker Compose (Recommended)

Using Docker Compose is the easiest way to get started with a fully functional Airflow environment:

```bash
# Create directories for DAGs, logs, and plugins
mkdir -p ./dags ./logs ./plugins ./config

# Download the docker-compose.yaml file
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'

# Initialize the environment
docker compose up airflow-init

# Start all services
docker compose up
```

Access the Airflow UI at `http://localhost:8080` with default credentials:

- Username: `airflow`
- Password: `airflow`

For more details, follow the [official Docker Compose guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

## Airflow 101: Basic Concepts

### DAGs (Directed Acyclic Graphs)

DAGs are the core concept in Airflow, representing workflows as collections of tasks with dependencies. The "directed" nature means tasks have a specific direction of flow, while "acyclic" ensures no circular dependencies exist, preventing infinite loops in your workflow.

#### Understanding DAGs

A DAG defines:

- The overall structure of your workflow
- Which tasks need to be executed
- The relationships and dependencies between tasks
- Execution schedule and timing constraints

Here's a simple DAG example:

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'tutorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t1 >> t2  # Set task dependency: t1 must run before t2
```

### Key Components

- **Tasks**: Individual units of work in a workflow. Each task is an instance of an operator and represents a single piece of work (e.g., execute a script, run an SQL query, or move data).

- **Operators**: Templates that define what work gets done. Common operators include:
  - `BashOperator`: Executes bash commands
  - `PythonOperator`: Calls Python functions
  - `SQLOperator`: Executes SQL commands
  - `EmailOperator`: Sends emails
  - `DockerOperator`: Executes commands in Docker containers

- **Task Dependencies**: Define the execution order of tasks using:
  - `>>` (downstream) and `<<` (upstream) operators
  - `set_upstream()` and `set_downstream()` methods
  - `[t1, t2] >> t3 >> [t4, t5]` for complex flows

- **Sensors**: Special operators that wait for conditions to be met:
  - `FileSensor`: Waits for a file to appear
  - `S3KeySensor`: Waits for a key in an S3 bucket
  - `HttpSensor`: Waits for an HTTP endpoint to be available
  - `SqlSensor`: Waits for a SQL query to return results

- **Hooks**: Interface to external systems (databases, APIs, cloud services) providing connection pooling and reuse.

For an in-depth understanding of Airflow fundamentals, refer to the [official tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html).

## Conclusion

This tutorial introduced Apache Airflow as a powerful workflow orchestration tool. To dive deeper into specific features and more advanced use cases, refer to the [official documentation](https://airflow.apache.org/docs/apache-airflow/stable/).
