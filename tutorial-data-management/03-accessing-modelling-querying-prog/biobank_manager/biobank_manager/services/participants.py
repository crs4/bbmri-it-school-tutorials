from biobank_manager.database.models import Participant
from biobank_manager.dtos.participants import ParticipantCreateDTO
from sqlalchemy.orm import Session



def add_participant(db:Session, participant_create_dto: ParticipantCreateDTO):
    participant = Participant(**participant_create_dto.model_dump())  # unpack DTO fields into model
    db.add(participant)
    db.commit()
    db.refresh(participant)  # refresh to get the auto-generated ID
    return participant