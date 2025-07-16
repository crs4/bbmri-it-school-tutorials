from fastapi import APIRouter, status

router = APIRouter(
  prefix="/participants",
  tags=["Participant"]
)

@router.get(
    "",
    description="Return a list of participants",
    status_code=status.HTTP_200_OK
)
def list_participants():
    return []


@router.get(
    "/{pid}",
    description="Return the participant with the id specified in input",
    status_code=status.HTTP_200_OK
)
def retrieve_participant(pid: int):
    return { "id": pid }

@router.post(
    "",
    description="Create a participant",
    status_code=status.HTTP_201_CREATED
)
def add_participant():
    return {}