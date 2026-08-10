from datetime import date as Date, time as Time
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


MIN_CUSTOM_INTERVAL_MINUTES = 15


LEGACY_INTERVAL_WORDS = {
    "Never",
    "Hourly",
    "Daily",
    "Weekly"
}


class EmailRequest(BaseModel):

    recipient: EmailStr

    subject: str

    message: str

    date: Date

    end_date: Optional[Date] = None

    time: Time

    attachments: List[str] = Field(default_factory=list)

    repeat_interval: Optional[str] = None

    attach_document: bool = False

    max_occurrences: Optional[int] = None


    @field_validator("end_date", mode="before")
    @classmethod
    def empty_end_date_to_none(cls, value):
        # Defense-in-depth: if an empty string reaches this model
        # directly (not just via app.py's `request.form.get(...) or
        # None` guard -- e.g. a future direct API call, or that
        # guard being changed later), treat it as "no end date"
        # instead of raising a confusing date-parsing error.
        if value == "":
            return None
        return value


    @field_validator("repeat_interval")
    @classmethod
    def validate_repeat_interval(cls, value):

        if value is None:
            return value


        if not isinstance(value, str):
            raise ValueError(
                "repeat_interval must be a string: "
                "'Never', 'Hourly', 'Daily', 'Weekly', "
                "or a number of minutes as a string."
            )


        value = value.strip()


        if value in LEGACY_INTERVAL_WORDS:
            return value


        try:
            minutes = int(value)

        except (ValueError, TypeError):
            raise ValueError(
                "repeat_interval must be "
                "Never, Hourly, Daily, Weekly "
                "or a number of minutes."
            )


        if minutes < MIN_CUSTOM_INTERVAL_MINUTES:
            raise ValueError(
                "Minimum custom interval is 15 minutes."
            )


        return value



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
    attachments: List[str] = Field(
        default_factory=list
        )



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
