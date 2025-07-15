# services/participants.py
from biobank_manager.database.repository import get_all_participants, get_participant_by_id

def list_participants(session):
  return get_all_participants(session)

def retrieve_participant_by_id(session):
  return get_participant_by_id(session)