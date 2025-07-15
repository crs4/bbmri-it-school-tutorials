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
    status_code=status.HTTP_200_OK
)
def list_participants(session: Session = Depends(get_db)):
    return part_services.list_participants(session)


@router.get(
    "/{pid}",
    description="Return the participant with the id specified in input",
    status_code=status.HTTP_200_OK
)
def retrieve_participant(pid: int, session: Session = Depends(get_db)):
    return part_services.retrieve_participant_by_id(session, pid)

@router.post(
    "",
    description="Create a participant",
    status_code=status.HTTP_201_CREATED
)
def add_participant():
    return {}