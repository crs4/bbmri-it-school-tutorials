import datetime
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import CreateSchema
from biobank_manager.conf import DATABASE_URL, DATABASE_SCHEMA_NAME
from biobank_manager.database.models import Base, Diagnosis, Participant, Sample
from names_generator import generate_name

from biobank_manager.database.repository import get_participant_id_by_first_name_and_last_name, get_samples_for_participant_by_id

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(CreateSchema(DATABASE_SCHEMA_NAME, if_not_exists=True))
    connection.commit()

Base.metadata.create_all(engine)

SAMPLE_TYPES = ["DNA", "RNA", "Blood", "Urine", "Feces", "Buffy Coat"]

DIAGNOSIS = [
    "Urinary tract infection",
    "Human immunodeficiency virus disease",
    "Sepsis",
    "Malignant neoplasm of breast",
    "Acute tonsillitis",
    "Acute appendicitis",
    "Streptococcus group A infection",
    "Iron deficiency anemia",
    "Hypocalcemia",
    "Fatty liver",
]
CREATE_DATA = False
if CREATE_DATA:
  # Data insert
  with Session(engine) as session:
    for participant_index in range(100):
        name, surname = generate_name(style="capital").split()
        gender = ["M", "F"][random.randint(0, 1)]
        date_of_birth = datetime.date(
            year=random.randint(1930, 2020),
            month=random.randint(1, 12),
            day=random.randint(1, 30),
        )
        participant = Participant(
            first_name=name,
            last_name=surname,
            gender=gender,
            date_of_birth=date_of_birth,
        )
        for sample_index in range(random.randint(1, 10)):
            sample_type = SAMPLE_TYPES[random.randint(0, len(SAMPLE_TYPES) - 1)]
            sample = Sample(
                type=sample_type,
                collection_date=datetime.datetime(
                    year=random.randint(date_of_birth.year, 2025),
                    month=random.randint(1, 12),
                    day=random.randint(1, 28),
                    hour=random.randint(0, 23),
                    minute=random.randint(0, 59),
                ),
                participant=participant,
            )

        for diagnosis_index in range(random.randint(0, 3)):
            diagnosis = Diagnosis(
                condition=DIAGNOSIS[random.randint(0, len(DIAGNOSIS) - 1)],
                date=datetime.datetime(
                    year=random.randint(date_of_birth.year, 2025),
                    month=random.randint(1, 12),
                    day=random.randint(1, 28),
                    hour=random.randint(0, 23),
                    minute=random.randint(0, 59),
                ),
            )

        session.add(participant)
        session.commit()


with Session(engine) as session:
  participant_id = get_participant_id_by_first_name_and_last_name(session, first_name="Funny", last_name="Davinci")
  print(f"Participant ID: {participant_id}")
  samples = get_samples_for_participant_by_id(session, participant_id)
  print(f"Participant has {len(samples)} samples of type {', '.join(s.type for s in samples)}")