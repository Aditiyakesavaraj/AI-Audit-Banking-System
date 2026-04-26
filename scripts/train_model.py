from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

df = pd.read_csv("data/sample_data.csv")

X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/trained_models/model.pkl")