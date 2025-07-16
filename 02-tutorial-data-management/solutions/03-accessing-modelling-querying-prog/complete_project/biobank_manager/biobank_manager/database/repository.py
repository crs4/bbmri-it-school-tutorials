from sqlalchemy import select
from sqlalchemy.orm import Session

from biobank_manager.database.models import Participant, Sample, Diagnosis


def get_all_participants(session: Session):
    stmt = select(Participant)
    return session.execute(stmt).scalars().all()


def get_participant_id_by_first_name_and_last_name(
    session: Session, first_name: str, last_name: str
):
    stmt = (
        select(Participant.id)
        .where(Participant.first_name == first_name)
        .where(Participant.last_name == last_name)
    )
    return session.execute(stmt).scalar()


def get_samples_for_participant_by_id(session: Session, id: int):
    stmt = select(Sample).where(Sample.participant_id == id)
    return session.execute(stmt).scalars().all()


def get_samples_for_participant_by_first_name_and_last_name(
    session: Session, first_name: str, last_name: str
):
    stmt = (
        select(Sample)
        .join(Participant)
        .where(Participant.first_name == first_name)
        .where(Participant.last_name == last_name)
    )
    return session.execute(stmt).scalars().all()


def get_samples_by_type(session, sample_types):
    stmt = select(Sample).where(Sample.type.in_(sample_types))
    return session.execute(stmt).scalars().all()


def get_diagnosis_for_participant_by_id(session, id):
    stmt = select(Diagnosis).where(Diagnosis.participant_id == id)
    return session.execute(stmt).scalars().all()


def get_diagnosis_before_date(session, date):
    stmt = select(Diagnosis).where(Diagnosis.date < date)
    return session.execute(stmt).scalars().all()
