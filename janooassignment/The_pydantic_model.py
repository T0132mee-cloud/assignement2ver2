from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime

class MedicationItem(BaseModel):
    name: str
    dosage: float  # We'll normalize "10mg" to 10.0
    unit: str = "mg"
    frequency: str  # e.g., "QD" (once daily), "BID" (twice daily)
    status: str = "ACTIVE" # ACTIVE or STOPPED

    @field_validator('name')
    @classmethod
    def normalize_name(cls, v: str) -> str:
        return v.strip().title() # "lisinopril " -> "Lisinopril"

    @field_validator('unit')
    @classmethod
    def normalize_unit(cls, v: str) -> str:
        return v.strip().lower()

class MedicationIngestRequest(BaseModel):
    patient_id: str
    clinic_id: str
    source: str # clinic_emr, hospital_discharge, or patient_reported
    medications: List[MedicationItem]
    collected_at: datetime = Field(default_factory=datetime.utcnow)