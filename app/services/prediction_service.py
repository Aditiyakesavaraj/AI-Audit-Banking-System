import joblib
import numpy as np

model = joblib.load("models/trained_models/model.pkl")

def predict(data: dict):
    features = np.array(list(data.values())).reshape(1, -1)
    result = model.predict(features)[0]
    return int(result)