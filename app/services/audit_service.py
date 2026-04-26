def audit(data, prediction):
    issues = []

    # Simple rule
    if data.get("income", 0) < 20000 and prediction == 1:
        issues.append("High risk approval")

    return {
        "issues": issues,
        "status": "OK" if not issues else "ALERT"
    }