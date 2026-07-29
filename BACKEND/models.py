from datetime import date, time
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

# For Scheduling Email
class EmailRequest(BaseModel):
    recipient: EmailStr
    subject: str
    message: str
    date: date
    end_date: Optional[date] = None
    time: time
    attachments: List[str] = []
    repeat_interval: Optional[str] = None
    attach_document: bool = False
    max_occurrences: Optional[int] = None

# For Sending Email Now
class SendNowRequest(BaseModel):
    recipient: EmailStr
    subject: str = Field(
        min_length=1,
        description="Email subject cannot be empty"
    )
    message: str = Field(
        min_length=1,
        description="Email message cannot be empty"
    )
    attachments: List[str] = []     

class TemplateRequest(BaseModel):
    name: str
    subject: str
    body: str
    last_edited: str

class SMTPRequest(BaseModel):
    smtp_host: str
    smtp_port: int
    sender_email: str
    app_password: str