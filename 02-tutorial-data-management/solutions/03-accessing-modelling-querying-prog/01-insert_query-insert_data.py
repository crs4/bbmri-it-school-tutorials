import datetime
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from biobank_manager.conf import DATABASE_URL
from biobank_manager.database.models import Diagnosis, Participant, Sample
from names_generator import generate_name
import calendar

engine = create_engine(DATABASE_URL)

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

with Session(engine) as session:
    print("Creating data")
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
        participant = Participant(
            first_name=name,
            last_name=surname,
            gender=gender,
            date_of_birth=date_of_birth
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
        print("Data created successfully")
