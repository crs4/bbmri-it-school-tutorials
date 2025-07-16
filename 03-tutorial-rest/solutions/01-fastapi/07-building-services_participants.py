# services/participants.py
from biobank_manager.database import repository

def list_participants(session):
  return repository.get_all_participants(session)

def retrieve_participant_by_id(session):
  return repository.get_participant_by_id(session)