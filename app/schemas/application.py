from datetime import date
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    company_name: str
    job_title: str
    status: str = "Applied"
    notes: str | None = None
    date_applied: date


class ApplicationResponse(BaseModel):
    id: int
    company_name: str
    job_title: str
    status: str
    notes: str | None
    date_applied: date

    class Config:
        from_attributes = True

class ApplicationUpdate(BaseModel):
    company_name: str
    job_title: str
    status: str
    notes: str | None = None
    date_applied: date


class ApplicationStatus(str, Enum):
    APPLIED = "Applied"
    ASSESSMENT = "Assessment"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"
    ACCEPTED = "Accepted"

status: ApplicationStatus = ApplicationStatus.APPLIED
status: ApplicationStatus