import joblib

def load_model():
    return joblib.load("models/trained_models/model.pkl")