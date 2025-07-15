from datetime import date
from enum import Enum, StrEnum
from typing import List
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped
from sqlalchemy.schema import MetaData
from biobank_manager.conf import DATABASE_SCHEMA_NAME
from sqlalchemy import Enum as SQLEnum  # Avoid conflict with Python's Enum
from datetime import datetime

metadata = MetaData(schema=DATABASE_SCHEMA_NAME)

Base = declarative_base(metadata=metadata)


class GenderEnum(StrEnum):
    MALE = "M"
    FEMALE = "F"
    UNKNOWN = "U"


class Participant(Base):
    __tablename__ = "participants"
    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str]
    first_name: Mapped[str]
    date_of_birth: Mapped[date]
    place_of_birth: Mapped[str]
    ssn: Mapped[str] = mapped_column(String(16))
    gender: Mapped[GenderEnum] = mapped_column(
        SQLEnum(GenderEnum, name="gender_enum", native_enum=False)
    )
    samples: Mapped[List["Sample"]] = relationship(
        back_populates="participant", cascade="all, delete-orphan"
    )
    diagnosis: Mapped[List["Diagnosis"]] = relationship(
        back_populates="participant", cascade="all, delete-orphan"
    )


class Sample(Base):
    __tablename__ = "samples"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    collection_date: Mapped[datetime] = mapped_column(nullable=False)
    participant: Mapped["Participant"] = relationship(
        "Participant", back_populates="samples"
    )
    participant_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(f"{DATABASE_SCHEMA_NAME}.participants.id"), nullable=False
    )


class Diagnosis(Base):
    __tablename__ = "diagnosis"
    id: Mapped[int] = mapped_column(primary_key=True)
    condition: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    severity: Mapped[str] = mapped_column(String, nullable=True)
    participant: Mapped["Participant"] = relationship(
        "Participant", back_populates="diagnosis"
    )
    participant_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(f"{DATABASE_SCHEMA_NAME}.participants.id"), nullable=False
    )
