# Apache Airflow Workflows Tutorial

## Introduction to Apache Airflow

Apache Airflow is an open-source platform for creating, scheduling, and
monitoring workflows programmatically. Developed by Airbnb in 2014 and later
donated to the Apache Software Foundation, Airflow allows you to define
workflows as code using Python, making them more maintainable, versionable, and
dynamic.

Airflow is widely used for automating ETL processes in industry.  There are also
other comparably valid alternative (e.g., if you're curious, see the [Awesome
ETL page](https://github.com/pawl/awesome-etl?tab=readme-ov-file#workflow-managementengines)).

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

For a comprehensive understanding of the architecture, refer to the [official
documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html).

## Installing Airflow

### Option 1: Deploy with Docker Compose

Using Docker Compose is the easiest way to get started with a complete Airflow environment.  It is a good basis for a production environment, though there are some security issues that need to be considered.

For the full procedure deployment, see the [official tutorial](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

TL;DR:
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


### Option 2: Standalone Airflow in pip in a uv virtual environment

This is a good option for a simple deployment for learning and experimenting,
but it requires using [`uv`](https://docs.astral.sh/uv/getting-started/installation/).

Refer to the [official documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html) for the full installation procedure.

Access the Airflow UI at `http://localhost:8080` with default credentials:

- Username: `airflow`
- Password: `airflow`


## Airflow 101: Basic Concepts

Complete the [Airflow fundamentals
tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html).
It will give you a basic understanding of the fundamental Airflow concepts --
e.g.,
* DAGs
* Operators
* Task dependencies
* Sensors
* Hooks

You will also find this knowledge useful if you decide to explore comparable workflow
managers that can be used to manage and automate the execution of ETL processes.


## Conclusion

This brief look at Airflow only scratches the surface of this powerful workflow
orchestration tool. If you decide that you may want to use Airflow for your own
work, dive deeper into specific features and more advanced use
cases in the [official
documentation](https://airflow.apache.org/docs/apache-airflow/stable/).
