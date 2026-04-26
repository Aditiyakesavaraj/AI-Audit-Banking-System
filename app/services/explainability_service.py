import shap
import joblib
import numpy as np

model = joblib.load("models/trained_models/model.pkl")
explainer = shap.Explainer(model)

def explain(data: dict):
    features = np.array(list(data.values())).reshape(1, -1)
    shap_values = explainer(features)

    return shap_values.values.tolist()