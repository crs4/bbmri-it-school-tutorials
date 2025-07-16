from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, computed_field

class ParticipantCreateDTO(BaseModel):
  prefix: Optional[str] = Field(title="An honorific prefix for the person (e.g., Dr.)", default=None)
  suffix: Optional[str] = Field(title="An honorific suffix for the person (e.g., MD.)", default=None)
  last_name: str = Field(title="Last name of the participant")
  first_name: str = Field(title="First name of the participant")
  date_of_birth: date = Field(title="Date of birth of the participant in ISO format (YYYY-MM-DD)")
  place_of_birth: str = Field(title="Place of birth of the participant")
  ssn: str = Field(title="Social Security Number of the participant")
  gender: str = Field("Gender of the participant")
 
class ParticipantReadDTO(ParticipantCreateDTO):
  id: int = Field(title="Unique identifier for the participant")
  
  @computed_field
  @property
  def name(self) -> str:
    return f"{self.first_name} {self.last_name}"
