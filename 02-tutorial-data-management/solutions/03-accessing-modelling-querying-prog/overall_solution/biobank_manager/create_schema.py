from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from biobank_manager.conf import DATABASE_URL, DATABASE_SCHEMA_NAME
from biobank_manager.database.models import Base

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(CreateSchema(DATABASE_SCHEMA_NAME, if_not_exists=True))
    connection.commit()

Base.metadata.create_all(engine)
