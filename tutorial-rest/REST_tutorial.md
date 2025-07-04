# REST API

In this tutorial we will see how interact with APIs

## Building a REST API with FastAPI

In this section we will create a REST API layer for the Database that we build in the [Data Management Tutorial](../tutorial-data-management/Data_Management_Tutorial.md)
We will create API calls for the objects samples, participants and diagnosis that we already developed (toghether with the related databaase) 
during the SQLAlchemy tutorial.
The rest API is composed of several levels of services, as per MVC pattern: 
- **Controllers**: they are the entry point of the API, they receive the requests and call the services to perform the operations
- **Services**: they contain the business logic of the application, they call the repositories to perform the operations on the database
- **DTOs**: they are the Data Transfer Objects, they are used to validate the data received from the API and to return the data to the client
1. Install FastAPI and uvicorn in the virtual env of the project
   
   **NB: remember to activate the virtualenv with `source venv/bin/activate`**

   ```bash
   pip install "fastapi[standard]"
   pip install uvicorn
   ```

2. In the biobank_manager project add the controllers package under the biobank_manager directory, with three files:
    - samples.py: it will contain the API calls for the samples
    - participants.py: it will contain the API calls for the participants
    - diagnosis.py: it will contain the API calls for the diagnosis

For example, for participants.py, the code will look like this:

```python
from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from biobank_manager.database import get_db  # your DB session dependency

from biobank_manager.services import participants
from biobank_manager.dtos.participants import ParticipantReadDTO, ParticipantCreateDTO

router = APIRouter(
    prefix="/participants",
    tags=["Participant"],
)


@router.post(
    "/",
    response_model=ParticipantReadDTO,
    response_description="Add a new participant",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
    response_model_exclude_unset=False,

)

def create_participant(
    participant_create_dto: ParticipantCreateDTO,
    db: Session = Depends(get_db)
):
    p = participants.add_participant(db, participant_create_dto
    )
    return p.to_participant_read_dto()
```
This code defines a FastAPI router for the participants API. It includes a POST endpoint to create a new participant, which uses a DTO for input validation and returns a DTO for the response.
Notide the call to the service (add_participant) that relates to what we will define at 4.

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

   from biobank_manager.conf import DATABASE_URL

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
   from biobank_manager.controllers.participants import router as participant_router

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


