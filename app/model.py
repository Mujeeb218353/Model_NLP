import joblib
from sentence_transformers import SentenceTransformer
import numpy as np

# Load models once
clf = joblib.load("app/model.joblib")
encoder = joblib.load("app/label_encoder.joblib")
bert_model = SentenceTransformer("app/bert_encoder")

def predict_gender(name: str):
    embedding = bert_model.encode([name])
    probs = clf.predict_proba(embedding)[0]
    pred_index = np.argmax(probs)
    pred_label = encoder.inverse_transform([pred_index])[0]
    confidence = round(probs[pred_index], 4)

    return {
        "name": name,
        "gender": pred_label,
        "confidence": confidence
    }