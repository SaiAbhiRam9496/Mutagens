# classifier.py
# Trains a small text classifier (TF-IDF + Logistic Regression) on your
# own example phrases, used as a fallback when rule-based parsing fails.

import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from training_data import TRAINING_DATA

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "intent_model.joblib")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.joblib")

def train():
    texts = [t for t, label in TRAINING_DATA]
    labels = [label for t, label in TRAINING_DATA]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=1000)
    model.fit(X, labels)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print(f"Trained on {len(texts)} examples. Model saved.")
    return model, vectorizer

def load_or_train():
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    return train()

def predict_intent(text, confidence_threshold=0.22):
    model, vectorizer = load_or_train()
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    best_idx = probs.argmax()
    best_label = model.classes_[best_idx]
    best_prob = probs[best_idx]

    if best_prob < confidence_threshold:
        return None  # not confident enough, let it stay "unknown"
    return best_label