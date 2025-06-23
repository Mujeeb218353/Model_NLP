# app/schema.py

from pydantic import BaseModel

class GenderRequest(BaseModel):
    name: str

class GenderResponse(BaseModel):
    name: str
    gender: str
    confidence: float