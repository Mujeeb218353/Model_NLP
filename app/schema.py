from pydantic import BaseModel

class ResumeRequest(BaseModel):
    resume_text: str

class PredictionResponse(BaseModel):
    profession: str
