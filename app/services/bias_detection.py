def check_bias(data):
    if data.get("gender") == "female":
        return "Check for gender bias"
    return "No bias detected"