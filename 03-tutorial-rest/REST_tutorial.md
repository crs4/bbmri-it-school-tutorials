# REST API

In this tutorial you will practice how to interact with REST APIs.

## Building a REST API with FastAPI

In this section you will extend the `biobank_manager` project that we built in the [Data Management Tutorial](../02-tutorial-data-management/Data_Management_Tutorial.md) by adding a REST API layer.

Remember that there is also a base for the data layer in the [solution directory](../02-tutorial-data-management/solutions/03-accessing-modelling-querying-prog/overall_solution/).

We will create API endpoints for the entities Samples, Participants and Diagnosis that we already developed (toghether with the related databaase) during the SQLAlchemy tutorial.

The REST API is composed of several levels of services: 
  - **Controllers**: they are the entrypoints of the API. They receive the requests from the client and call the services to perform the operations
  - **Services**: they contain the business logic of the application. They call the repositories to perform the operations on the database
  - **DTOs**: they are the Data Transfer Objects, the classes used to model the bodies of the requests and the responses of the API. 

### Steps 

1. First of all we must install FastAPI and Uvicorn in the virtualenv of the project
   
   **NB: remember to activate the virtualenv with `source venv/bin/activate`**

   ```bash
   pip install "fastapi[standard]"
   ```

1. The second step is to initialize our REST API. Edit the `biobank_manager/__init__.py` file with the following code

   ```python
   from fastapi import FastAPI

   app = FastAPI(
     title="Biobank Manager API",
     version="1.0.0",
     description="Biobank manager API for managing biobank data",
   )

   @app.get("/")
   def home():
     return {"message": f"Hello to {app.title}"}
   ```

   This code, simply creates the app and the first endpoint: the `home` function will respond to `GET /` requests by returning
   a JSON response with a welcome message

1. Ok now we need to serve the REST API so it can be exposed via network. To do that a common solution is [Uvicorn](https://www.uvicorn.org/) which a ASGI web server. Install it as usual with pip

   ```bash
   pip install uvicorn
   ```

1. Now we can add a `__main__.py` in the `biobank_manager` directory that simply run uvicorn which exposes the API

   ```python
   import uvicorn

   if __name__ == "__main__":
       uvicorn.run("biobank_manager:app", host="127.0.0.1", port=8000, reload=True)
   ```

   This command runs uvicorn and exposes a web server on the port 8000 of the local interface. Which application is handling the requests? Of course, the object `app` in the `biobank_manager` package, i.e., the FastAPI `app` instance that we created in the `__init__.py`.

   From the `main` directory, run the module 

   ```bash
   $ python -m biobank_manager
   INFO:     Will watch for changes in these directories: ['~/biobank_manager']
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [341658] using WatchFiles
   INFO:     Started server process [341678]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```
  
   Now navigate with a browser to `http://localhost:8000`, you should obtain as response the `json` 

   ```json
   { "message": "Hello to Biobank Manager API" }
   ```

1. We can start now to implement the endpoints for the Participants entities. We will need to create some objects:
   
   - the `controller`: the functions that handle the request for a specific endpoint
   - the `dtos`: the models of the request and response
   - the `service`: the business logic modules that create an interface between the controller and the database.
   
   Of course, we need also the `database` module, but we already created it in the prviouse tutorial.

   Let's create the directories for these objects with the module files

   ```
   biobank_manager/
     controllers/
       __init__.py
       participants.py
     dtos/
       __init__.py
       participants.py
     services/
       __init__.py
       participants.py
   ```

1. Let's implement the first endpoint. To get all the participants. Edit the file `controllers/participants.py` with the following code
   
   ```python
   from fastapi import APIRouter, status

   router = APIRouter(
     prefix="/participants",
     tags=["Participant"]
   )

   @router.get(
       "",
       description="Return a list of participants",
       status_code=status.HTTP_200_OK
   )
   def list_participants():
       return []

   @router.get(
       "/{pid}",
       description="Return the participant with the id specified in input",
       status_code=status.HTTP_200_OK
   )
   def retrieve_participant(pid: int):
       return { "id": pid }

   @router.post(
       "",
       description="Create a participant",
       status_code=status.HTTP_201_CREATED
   )
   def add_participant():
       pass
   ```

   This code defines a FastAPI router for the participants API. A router is used to handle a part of the API. It is usefult to split the API in small pieces so it's easier to maintain.
   
   The module creates three endpoints to handle:

   - `GET /participants`: return the list of participants
   - `GET /participants/{pid}`: return the specific participant with id `pid`
   - `POST /participants`: create a participant

   Notice the function `retrieve_participant`: the signature has a `pid` parameter with the same name of the parameter between brackets `{}` in the url of the endpoint `"{pid}"`. FastAPI will set the value of the parameter in the function, with the value sent by the client. For example the HTTP call
   
   ```http
   GET /participants/123
   ```

   Will pass `123` as the value of the pid argument of the `retrieve_participant` function.

   Two more things can be noted:
    - the `response_status_code` parameter of the `@router` decorator: it indicates the default status code returned if the operation is successfull (i.e., no exceptions are raised)
    - the `description` parameter of `@router` decorator: FastAPI use it for the swagger documentation of the API

   Before trying the endpoints, we need to tell the `app` objects that there is a router that handles the `/participants` sub-endpoints. To do that, edit the `biobank_manager/__init__.py` file to
   - add an import statement for the router 
   - call the `app.include_router` method of the FastAPI class to add the router

   ```python
   from biobank_manager.controllers.participants import router as participant_router
   ...
   app = FastAPI(
     title="Biobank Manager API",
     version="1.0.0",
     description="Biobank manager API for managing biobank data",
   )

   app.include_router(participant_router)
   ```

3. In the same way, create a new package called dtos under the biobank_manager directory, with three files:
    - samples.py: it will contain the DTO models for the samples
    - participants.py: it will contain the DTO models for the participants
    - diagnosis.py: it will contain the DTO models for the diagnosis

   The DTO models are related to the API input and output operations: it means that when an endpoint, for example 
   a POST to add new samples, will receive the data from the incoming request, it will use the DTO model to validate the data.
   In the same way, there will be a DTO model to return the data to the client.
   For example, in the DTO module for the participants, there will be:

   ```python
   class ParticipantCreateDTO(BaseModel):
     last_name: str = Field(title="Last name of the participant")
     first_name: str = Field(title="First name of the participant")
     date_of_birth: date = Field(title="Date of birth of the participant in ISO format (YYYY-MM-DD)")
     place_of_birth: str = Field(title="Place of birth of the participant")
     ssn: str = Field(title="Social Security Number of the participant")
     gender: str = Field("Gender of the participant")
 
   class ParticipantReadDTO(ParticipantCreateDTO):
     id: int = Field(title="Unique identifier for the participant")
     model_config = ConfigDict(from_attributes=True)   
    ```
    
   Notice that we do not want to set the IDs in the DTOs, because they are generated by the database. To do that, 
   remember to assign the attribute "autoincrement=True" to the id field in the SQLAlchemy model, so that the database will generate the ID automatically.
   The `model_config = ConfigDict(from_attributes=True)` is used to allow the DTO to be created from the SQLAlchemy model.

4. Now, create a new package called services under the biobank_manager directory, with three files:
    - samples.py: it will contain the services for the samples
    - participants.py: it will contain the services for the participants
    - diagnosis.py: it will contain the services for the diagnosis
   
    The services will contain the business logic of the application, they will perform operations on the database.
    For example, in the services module for the participants, there will be:
    ```python
   from biobank_manager.database.models import Participant
   from biobank_manager.dtos.participants import ParticipantCreateDTO
   from sqlalchemy.orm import Session

   def add_participant(db:Session, participant_create_dto: ParticipantCreateDTO):
      participant = Participant(**participant_create_dto.model_dump())  # unpack DTO fields into model
      db.add(participant)
      db.commit()
      db.refresh(participant)  # refresh to get the auto-generated ID
      return participant
5. Now, notice that both controller and participant service use this db object, that refers to the
   logic used by SqlAlchemy to interact with the database. Actually we don't have created it yet,
   let's do it by adding the following code to the database/__init__.py file:
   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.orm import sessionmaker, Session
   from sqlalchemy.ext.declarative import declarative_base

   from biobank_manager import DATABASE_URL

   engine = create_engine(DATABASE_URL, echo=True)

   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

   Base = declarative_base()

   def get_db() -> Session:
      db = SessionLocal()
      try:
        yield db  # use as a generator for cleanup
      finally:
        db.close()
   ```
   Notice that this configuration will be valid for all the APIs and all the related objects.
   In order to test this API for participants, what is missing right not is to add the modules
   that will run the FastAPI application. 
6. Create a new file called app.py in the biobank_manager directory with the following code:
   ```python
   from contextlib import asynccontextmanager
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware
   from biobank_manager.database import Base, engine
   from biobank_manager import router as participant_router

    app = FastAPI(
       title="Biobank Manager API",
       version="1.0.0",
       description="Biobank manager API for managing biobank data",
    )
   
   @asynccontextmanager
   async def lifespan(app: FastAPI):
      Base.metadata.create_all(bind=engine)
      yield

   app = FastAPI(lifespan=lifespan)
   app.include_router(participant_router, prefix="/api", tags=["Participants"])

   ```
    This code initializes the FastAPI application, includes the participants router,
   and sets up the database tables at startup. Notice that you will have to add the other routers
   for samples and diagnosis in the same way as the participants router (app.include_router calls).
7. Create now a run module to run the FastAPI application, for example in a file called start_api_server.py:
   ```python
   import uvicorn
   if __name__ == "__main__":
      uvicorn.run("biobank_manager.app:app", host="127.0.0.1", port=8000, reload=True)
    ```
   Set the host and port values accordingly. 
8. Run the API server with the following command:
   ```bash
   python start_api_server.py
   ```
9. Now, let's test the only endpoint that we have created so far, the one to add a new participant.
   You can use a tool like Postman or the python requests library to test the API.
   Make a POST request to the endpoint http://[host]:[port]/api/participants/ with the following JSON body:
   ```json
   {
      "last_name": "Doe",
      "first_name": "John",
      "date_of_birth": "1990-01-01",
      "place_of_birth": "New York",
      "ssn": "DOEJHN90A01Z404E",
      "gender": "M"
   }
    ```
    If everything is set up correctly, you should receive a response with the created participant object, including the auto-generated ID:
       ```json
   {
      "last_name": "Doe",
      "first_name": "John",
      "date_of_birth": "1990-01-01",
      "place_of_birth": "New York",
      "ssn": "DOEJHN90A01Z404E",
      "gender": "M"
      "id": [progressively generated ID in your local database environment]
   }
    ```
10. Try to make the POST above twice, then check the database. What happens? Try to change the code 
    in a way to avoid this issue. 
11. Let's force a bad request, for example by missing the last_name field in the JSON body. 


