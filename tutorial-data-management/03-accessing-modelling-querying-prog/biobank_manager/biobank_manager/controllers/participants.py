from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from biobank_manager.database import get_db  # your DB session dependency

from biobank_manager.services import participants
from biobank_manager.dtos.participants import ParticipantReadDTO, ParticipantCreateDTO

router = APIRouter(
    prefix="/participants",
    tags=["Participant"],
)


@router.post(
    "/",
    response_model=ParticipantReadDTO,
    response_description="Add a new participant",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
    response_model_exclude_unset=False,

)

def create_participant(
    participant_create_dto: ParticipantCreateDTO,
    db: Session = Depends(get_db)
):
    p = participants.add_participant(db, participant_create_dto
    )
    return p.to_participant_read_dto()


