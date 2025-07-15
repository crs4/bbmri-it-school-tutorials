from typing import List
from biobank_manager.dtos.participants import ParticipantCreateDTO, ParticipantReadDTO
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from biobank_manager.database import get_db
from biobank_manager.services import participants as part_services

router = APIRouter(
  prefix="/participants",
  tags=["Participant"]
)

@router.get(
    "",
    description="Return a list of participants",
    status_code=status.HTTP_200_OK,
    response_model=List[ParticipantReadDTO]
)
def list_participants(session: Session = Depends(get_db)):
    return part_services.get_all_participants(session)


@router.get(
    "/{pid}",
    description="Return the participant with the id specified in input",
    status_code=status.HTTP_200_OK,
    response_model=ParticipantReadDTO
)
def retrieve_participant(pid: int, session: Session = Depends(get_db)):
    return part_services.get_participant_by_id(session, pid)

@router.post(
    "",
    description="Create a participant",
    status_code=status.HTTP_201_CREATED,
    response_model=ParticipantReadDTO
)
def add_participant(data: ParticipantCreateDTO, session: Session = Depends(get_db)):
    return part_services.create_participant(session, data)