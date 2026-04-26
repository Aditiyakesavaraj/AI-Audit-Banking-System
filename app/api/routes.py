from fastapi import APIRouter
from app.services.prediction_service import predict
from app.services.explainability_service import explain
from app.services.audit_service import audit

router = APIRouter()

@router.post("/predict")
def run_prediction(data: dict):
    prediction = predict(data)
    explanation = explain(data)
    audit_result = audit(data, prediction)

    return {
        "prediction": prediction,
        "explanation": explanation,
        "audit": audit_result
    }