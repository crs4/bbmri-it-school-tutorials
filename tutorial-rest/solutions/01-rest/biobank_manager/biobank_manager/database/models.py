from datetime import date
from enum import Enum, StrEnum
from typing import List
<<<<<<< HEAD:tutorial-data-management/Solutions/03-accessing-modelling-querying-prog/5-database_creation-models.py
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped
from sqlalchemy.schema import MetaData
from biobank_manager.conf import DATABASE_SCHEMA_NAME
from sqlalchemy import Enum as SQLEnum  # Avoid conflict with Python's Enum
from datetime import datetime
=======
from sqlalchemy import Column, Date, Integer, String, ForeignKey, DateTime, Enum as SAEnum
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped
from sqlalchemy.schema import MetaData
from biobank_manager.conf import DATABASE_SCHEMA_NAME
from biobank_manager.dtos.participants import ParticipantReadDTO
>>>>>>> 4508d509acc9faa1bc2764680ae1f3f4f1535e42:tutorial-rest/solutions/01-rest/biobank_manager/biobank_manager/database/models.py

metadata = MetaData(schema=DATABASE_SCHEMA_NAME)

Base = declarative_base(metadata=metadata)


class GenderEnum(StrEnum):
    MALE = "M"
    FEMALE = "F"


class Participant(Base):
    __tablename__ = "participants"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str]
    first_name: Mapped[str]
    date_of_birth: Mapped[date]
<<<<<<< HEAD:tutorial-data-management/Solutions/03-accessing-modelling-querying-prog/5-database_creation-models.py
    gender: Mapped[GenderEnum] = mapped_column(
        SQLEnum(GenderEnum, name="gender_enum", native_enum=False)
    )
=======
    place_of_birth: Mapped[str]
    ssn: Mapped[str] = mapped_column(String(16)) 
    gender: Mapped[GenderEnum] = mapped_column(
    SAEnum(GenderEnum, name="gender_enum", validate_strings=True)
)
>>>>>>> 4508d509acc9faa1bc2764680ae1f3f4f1535e42:tutorial-rest/solutions/01-rest/biobank_manager/biobank_manager/database/models.py
    samples: Mapped[List["Sample"]] = relationship(
        back_populates="participant", cascade="all, delete-orphan"
    )
    diagnosis: Mapped[List["Diagnosis"]] = relationship(
        back_populates="participant", cascade="all, delete-orphan"
    )
    def to_participant_read_dto(self):
        return ParticipantReadDTO.model_validate(self)


class Sample(Base):
    __tablename__ = "samples"
<<<<<<< HEAD:tutorial-data-management/Solutions/03-accessing-modelling-querying-prog/5-database_creation-models.py
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    collection_date: Mapped[datetime] = mapped_column(nullable=False)
    participant: Mapped["Participant"] = relationship(
        "Participant", back_populates="samples"
    )
    participant_id: Mapped[int] = mapped_column(
=======
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    collection_date = Column(DateTime, nullable=False)
    participant = relationship("Participant", back_populates="samples")
    participant_id = Column(
>>>>>>> 4508d509acc9faa1bc2764680ae1f3f4f1535e42:tutorial-rest/solutions/01-rest/biobank_manager/biobank_manager/database/models.py
        Integer, ForeignKey(f"{DATABASE_SCHEMA_NAME}.participants.id"), nullable=False
    )


class Diagnosis(Base):
    __tablename__ = "diagnosis"
<<<<<<< HEAD:tutorial-data-management/Solutions/03-accessing-modelling-querying-prog/5-database_creation-models.py
    id: Mapped[int] = mapped_column(primary_key=True)
    condition: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    severity: Mapped[str] = mapped_column(String, nullable=True)
    participant: Mapped["Participant"] = relationship(
        "Participant", back_populates="diagnosis"
    )
    participant_id: Mapped[int] = mapped_column(
=======
    id = Column(Integer, primary_key=True, autoincrement=True)
    condition = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    severity = Column(String, nullable=True)
    participant = relationship("Participant", back_populates="diagnosis")
    participant_id = Column(
>>>>>>> 4508d509acc9faa1bc2764680ae1f3f4f1535e42:tutorial-rest/solutions/01-rest/biobank_manager/biobank_manager/database/models.py
        Integer, ForeignKey(f"{DATABASE_SCHEMA_NAME}.participants.id"), nullable=False
    )

