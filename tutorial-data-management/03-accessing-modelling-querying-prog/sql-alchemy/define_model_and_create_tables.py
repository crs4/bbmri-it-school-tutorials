from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, text, DateTime
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.schema import MetaData

from conf import DATABASE_URL


engine = create_engine(DATABASE_URL, echo=True)

schema_name = "sql_alchemy_test"
quoted_schema = f'"{schema_name}"'

metadata = MetaData(schema=schema_name)
Base = declarative_base(metadata=metadata)

class Donor(Base):
    __tablename__ = "donors"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    gender = Column(String, nullable=False)
    samples = relationship("Sample", back_populates="donor", cascade="all, delete-orphan")

class Sample(Base):
    __tablename__ = "samples"
    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey(f'{schema_name}.donors.id'), nullable=False)
    sample_type = Column(String, nullable=False)
    collection_date = Column(DateTime, nullable=False)
    donor = relationship("Donor", back_populates="samples")

Base.metadata.create_all(engine)