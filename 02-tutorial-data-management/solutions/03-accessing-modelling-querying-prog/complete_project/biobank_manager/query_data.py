import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from biobank_manager.conf import DATABASE_URL

from biobank_manager.database.repository import (
    get_all_participants,
    get_participant_id_by_first_name_and_last_name,
    get_samples_for_participant_by_id,
    get_samples_for_participant_by_first_name_and_last_name,
    get_samples_by_type,
    get_diagnosis_for_participant_by_id,
    get_diagnosis_before_date,
)

engine = create_engine(DATABASE_URL)

with Session(engine) as session:
    print("Get all participants")
    participants = get_all_participants(session)
    print(f"Found {len(participants)}")

    first_name = participants[0].first_name
    last_name = participants[0].last_name
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
