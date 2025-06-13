from fastapi import FastAPI
from app.schema import ResumeRequest, PredictionResponse
from app.model import predict_profession

app = FastAPI(title="Resume Profession Predictor", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Resume NLP API is up and running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(req: ResumeRequest):
    profession = predict_profession(req.resume_text)
    return PredictionResponse(profession=profession)
