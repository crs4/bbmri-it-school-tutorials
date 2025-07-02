from datetime import datetime, timedelta
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import define_model_and_create_tables as model

from conf import DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)


first_names = ["Alice", "Bob", "Carol", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis", "Wilson", "Moore", "Taylor"]
genders = ["Male", "Female", "Other"]
sample_types = ["Blood", "Saliva", "Urine", "Tissue"]

def random_date(start_year=1950, end_year=2000):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_collection_date():
    now = datetime.now()
    return now - timedelta(days=random.randint(1, 1000))

Session = sessionmaker(bind=engine)
session = Session()

donors = []
samples = []

for i in range(20):
    donor = model.Donor(
        first_name=random.choice(first_names),
        last_name=random.choice(last_names),
        date_of_birth=random_date(),
        gender=random.choice(genders)
    )
    donors.append(donor)
    session.add(donor)

session.flush()

total_samples = 70
for donor in donors:
    num_samples = random.randint(1, 6)
    for _ in range(min(num_samples, total_samples)):
        sample = model.Sample(
            donor_id=donor.id,
            sample_type=random.choice(sample_types),
            collection_date=random_collection_date()
        )
        samples.append(sample)
        session.add(sample)
        total_samples -= 1
        if total_samples <= 0:
            break
    if total_samples <= 0:
        break

session.commit()
print("Data populated successfully!")