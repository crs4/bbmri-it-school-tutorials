import datetime
import os
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import CreateSchema
from biobank_manager.conf import DATABASE_URL, DATABASE_SCHEMA_NAME
from biobank_manager.database.models import Base, Diagnosis, Participant, Sample

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(CreateSchema(DATABASE_SCHEMA_NAME, if_not_exists=True))
    connection.commit()

Base.metadata.create_all(engine)

create_data_str = os.getenv("CREATE_DATA", "false").lower()
CREATE_DATA = create_data_str in ["true"]
print(
    f"CREATE_DATA is set to {CREATE_DATA}. Data will {'be' if CREATE_DATA else 'not be'} created."
)
if CREATE_DATA:
    # Data insert
    pass
