from biobank_manager.database import repository
from biobank_manager.dtos.participants import ParticipantCreateDTO

def list_participants(session):
  return repository.get_all_participants(session)

def retrieve_participant_by_id(session, id):
  return repository.get_participant_by_id(session, id)
    
def create_participant(session, participant_data: ParticipantCreateDTO):
    db_data = participant_data.model_dump()
    del db_data["prefix"]
    del db_data["suffix"]
    return repository.create_participant(session, db_data)