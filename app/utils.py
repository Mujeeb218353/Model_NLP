import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sentence_transformers import SentenceTransformer
import joblib

def train_and_save_model():
    df = pd.read_csv("Resume.csv")
    df.dropna(subset=["Resume_str", "Category"], inplace=True)

    encoder = LabelEncoder()
    y = encoder.fit_transform(df["Category"])

    model = SentenceTransformer("all-MiniLM-L6-v2")
    X = model.encode(df["Resume_str"].tolist(), show_progress_bar=True)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)

    joblib.dump(clf, "app/model.joblib")
    joblib.dump(encoder, "app/label_encoder.joblib")
    joblib.dump(model, "app/bert_encoder.joblib")
