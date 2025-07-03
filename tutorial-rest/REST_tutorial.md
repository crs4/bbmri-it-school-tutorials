# REST API

In this tutorial we will see how interact with APIs

## Building a REST API with FastAPI

In this section we will create a REST API layer for the Database that we build in the [Data Management Tutorial](../tutorial-data-management/Data_Management_Tutorial.md)

1. Install FastAPI in the virtual env of the project
   
   **NB: remember to activate the virtualenv with `source venv/bin/activate`**

   ```bash
   pip install "fastapi[standard]"
   ```

1. In the biobank_manager project add the controllers modules with three files
