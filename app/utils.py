import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sentence_transformers import SentenceTransformer
import joblib

def train_and_save_model():
    try:
        # Load dataset
        df = pd.read_csv("data.csv")
        df.dropna(subset=["Name", "Gender"], inplace=True)
        df["Name"] = df["Name"].astype(str).str.strip()

        print(f"[INFO] Loaded dataset with {len(df)} records.")

        # Encode gender labels
        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(df["Gender"])
        print("[INFO] Gender labels encoded.")

        # Load BERT model
        bert_model = SentenceTransformer("all-MiniLM-L6-v2")
        print("[INFO] BERT model loaded.")

        # Convert names to BERT embeddings
        names = df["Name"].tolist()
        X = bert_model.encode(names, show_progress_bar=True)
        print("[INFO] Name embeddings created.")

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Train Logistic Regression classifier
        clf = LogisticRegression(max_iter=1000)
        clf.fit(X_train, y_train)
        print("[INFO] Logistic Regression model trained.")

        # Evaluate
        y_pred = clf.predict(X_test)
        print("\n[METRICS]")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))
        print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

        # Save everything
        os.makedirs("app", exist_ok=True)
        joblib.dump(clf, "app/model.joblib")
        joblib.dump(label_encoder, "app/label_encoder.joblib")
        bert_model.save("app/bert_encoder")

        print("[INFO] Model, encoder, and BERT embeddings saved to 'app/'.")

    except Exception as e:
        print(f"[ERROR] {str(e)}")

train_and_save_model()