from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class ParticipantCreateDTO(BaseModel):
    """
    Data Transfer Object for participant information.
    """

    last_name: str = Field(title="Last name of the participant")
    first_name: str = Field(title="First name of the participant")
    date_of_birth: date = Field(title="Date of birth of the participant in ISO format (YYYY-MM-DD)")
    place_of_birth: str = Field(title="Place of birth of the participant")
    ssn: str = Field(title="Social Security Number of the participant")
    gender: str = Field("Gender of the participant")

class ParticipantReadDTO(ParticipantCreateDTO):
    """
    Data Transfer Object for creating a new participant.
    """
    id: int = Field(title="Unique identifier for the participant")

    model_config = ConfigDict(from_attributes=True)
