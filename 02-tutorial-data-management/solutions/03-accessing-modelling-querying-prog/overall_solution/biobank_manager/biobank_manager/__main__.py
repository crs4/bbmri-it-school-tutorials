import datetime
import os
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import CreateSchema
from biobank_manager.conf import DATABASE_URL, DATABASE_SCHEMA_NAME
from biobank_manager.database.models import Base, Diagnosis, Participant, Sample
from names_generator import generate_name
from codicefiscale import codicefiscale
import calendar

from biobank_manager.database.repository import (
    get_participant_id_by_first_name_and_last_name,
    get_samples_for_participant_by_id,
    get_samples_for_participant_by_first_name_and_last_name,
    get_samples_by_type,
    get_diagnosis_for_participant_by_id,
    get_diagnosis_before_date,
)

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

COMUNI = [
    "Roma",
    "Milano",
    "Napoli",
    "Torino",
    "Palermo",
    "Genova",
    "Bologna",
    "Firenze",
    "Cagliari",
    "Bari",
    "Venezia",
]
create_data_str = os.getenv("CREATE_DATA", "false").lower()
CREATE_DATA = create_data_str in ["true"]
print(
    f"CREATE_DATA is set to {CREATE_DATA}. Data will {'be' if CREATE_DATA else 'not be'} created."
)
if CREATE_DATA:
    # Data insert
    with Session(engine) as session:
        for participant_index in range(100):
            name, surname = generate_name(style="capital").split()
            gender = ["M", "F"][random.randint(0, 1)]
            year = random.randint(1930, 2020)
            month = random.randint(1, 12)
            if month in [4, 6, 9, 11]:
                day = random.randint(1, 30)
            elif month == 2:
                if calendar.isleap(year):
                    day = random.randint(1, 29)
                else:
                    day = random.randint(1, 28)
            else:
                day = random.randint(1, 31)

            date_of_birth = datetime.date(
                year=year,
                month=month,
                day=day,
            )
            # place_of_birth = random.choice(COMUNI)
            participant = Participant(
                first_name=name,
                last_name=surname,
                gender=gender,
                date_of_birth=date_of_birth,
                # place_of_birth=place_of_birth,
                # ssn=codicefiscale.encode(
                #     lastname=surname,
                #     firstname=name,
                #     gender=gender,
                #     birthdate=str(date_of_birth),
                #     birthplace=place_of_birth,
                # ),
            )
            for sample_index in range(random.randint(1, 10)):
                sample_type = SAMPLE_TYPES[random.randint(0, len(SAMPLE_TYPES) - 1)]
                month = random.randint(1, 12)
                if month in [4, 6, 9, 11]:
                    day = random.randint(1, 30)
                elif month == 2:
                    if calendar.isleap(year):
                        day = random.randint(1, 29)
                    else:
                        day = random.randint(1, 28)
                else:
                    day = random.randint(1, 31)
                sample = Sample(
                    type=sample_type,
                    collection_date=datetime.datetime(
                        year=random.randint(date_of_birth.year, 2025),
                        month=month,
                        day=day,
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
                    severity=random.choice(["None", "Mild", "Moderate", "Severe"]),
                    participant=participant,
                )

            session.add(participant)
            session.commit()


with Session(engine) as session:
    first_name = "Flamboyant"
    last_name = "Lumiere"
    print(f"Searching for participant {first_name} {last_name}...")
    participant_id = get_participant_id_by_first_name_and_last_name(
        session, first_name=first_name, last_name=last_name
    )
    print(f"Participant ID: {participant_id}")
    samples = get_samples_for_participant_by_id(session, participant_id)
    print(
        f"Participant has {len(samples)} samples of type {', '.join(s.type for s in samples)}"
    )
    samples = get_samples_for_participant_by_first_name_and_last_name(
        session, first_name=first_name, last_name=last_name
    )
    print(
        f"Participant {first_name} {last_name} has {len(samples)} samples of type {', '.join(s.type for s in samples)}"
    )
    samples = get_samples_by_type(session, ["DNA", "RNA"])
    print(f"Found {len(samples)} samples of type DNA or RNA")

    samples = get_samples_by_type(session, ["DNA"])
    print(f"Found {len(samples)} samples of type DNA")

    samples = get_samples_by_type(session, ["RNA"])
    print(f"Found {len(samples)} samples of type RNA")

    diagnosis = get_diagnosis_for_participant_by_id(session, participant_id)

    print(f"Participant {first_name} {last_name} has {len(diagnosis)} diagnosis")
    for d in diagnosis:
        print(
            f"Diagnosis: {d.condition}, Date: {d.date}, Severity: {d.severity if d.severity else 'N/A'}"
        )

    diagnosis = get_diagnosis_before_date(session, datetime.datetime(2020, 1, 1))
    print(f"Found {len(diagnosis)} diagnosis before 2020-01-01")
    for d in diagnosis:
        print(
            f"Diagnosis: {d.condition}, Date: {d.date}, Severity: {d.severity if d.severity else 'N/A'}"
        )
