from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conf import DATABASE_URL
import define_model_and_create_tables as model

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

first_name = "Carol"
last_name = "Wilson"

donor = session.query(model.Donor).filter_by(first_name=first_name, last_name=last_name).first()

if donor:
    print(f"Samples for donor {donor.first_name} {donor.last_name} (ID: {donor.id}):")
    for sample in donor.samples:
        print(f"  - Sample ID: {sample.id}, Type: {sample.sample_type}, Collected: {sample.collection_date}")
else:
    print(f"No donor found with name {first_name} {last_name}")