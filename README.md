# Resume Profession Prediction API

This project uses a BERT-based model to predict profession categories based on resume text using FastAPI.

## Steps to Run

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Train the model:
```bash
python -c "from app.utils import train_and_save_model; train_and_save_model()"
```

3. Start the API:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Visit Swagger docs at `http://localhost:8000/docs`
