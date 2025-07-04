from typing import Optional

from pydantic import BaseModel, Field


class SampleCreateDTO(BaseModel):
    """
    Data Transfer Object for creating a sample.
    """
    sample_type: str = Field(title="Type of the sample, e.g., blood, urine")
    collection_date: str = Field(title="Date when the sample was collected, in ISO format (YYYY-MM-DD)")
    volume: Optional[float] = Field(title="Volume of the sample in milliliters")
    donor_id: str = Field(title="Unique identifier for the participant related to the sammple")

class SampleReadDTO(SampleCreateDTO):
    id: int = Field(title="Unique identifier for the sample")