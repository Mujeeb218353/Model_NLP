import joblib

clf = joblib.load("app/model.joblib")
encoder = joblib.load("app/label_encoder.joblib")
model = joblib.load("app/bert_encoder.joblib")

def predict_profession(resume_text: str) -> str:
    embedding = model.encode([resume_text])[0]
    pred = clf.predict([embedding])[0]
    return encoder.inverse_transform([pred])[0]
