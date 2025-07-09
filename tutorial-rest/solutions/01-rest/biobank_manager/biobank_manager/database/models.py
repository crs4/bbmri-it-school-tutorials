from datetime import date
from enum import Enum, StrEnum
from typing import List
from sqlalchemy import Column, Date, Integer, String, ForeignKey, DateTime, Enum as SAEnum
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped
from sqlalchemy.schema import MetaData
from biobank_manager.conf import DATABASE_SCHEMA_NAME
from biobank_manager.dtos.participants import ParticipantReadDTO

metadata = MetaData(schema=DATABASE_SCHEMA_NAME)

Base = declarative_base(metadata=metadata)

class GenderEnum(StrEnum):
    MALE = "M"
    FEMALE = "F"
    UNKNOWN = "U"

class Participant(Base):
    __tablename__ = "participants"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str]
    first_name: Mapped[str]
    date_of_birth: Mapped[date]
    place_of_birth: Mapped[str]
    ssn: Mapped[str] = mapped_column(String(16)) 
    gender: Mapped[GenderEnum] = mapped_column(
    SAEnum(GenderEnum, name="gender_enum", validate_strings=True)
)
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
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    collection_date = Column(DateTime, nullable=False)
    participant = relationship("Participant", back_populates="samples")
    participant_id = Column(
        Integer, ForeignKey(f"{DATABASE_SCHEMA_NAME}.participants.id"), nullable=False
    )


class Diagnosis(Base):
    __tablename__ = "diagnosis"
    id = Column(Integer, primary_key=True, autoincrement=True)
    condition = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    severity = Column(String, nullable=True)
    participant = relationship("Participant", back_populates="diagnosis")
    participant_id = Column(
        Integer, ForeignKey(f"{DATABASE_SCHEMA_NAME}.participants.id"), nullable=False
    )
