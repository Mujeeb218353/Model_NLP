from fastapi import FastAPI
from app.schema import GenderRequest, GenderResponse
from app.model import predict_gender

app = FastAPI(title="Gender Predictor by Name", version="1.0")

@app.get("/")
def read_root():
    return {"message": "🎉 Gender Prediction API is up and running!"}

@app.post("/predict", response_model=GenderResponse)
def predict(req: GenderRequest):
    return predict_gender(req.name)