from fastapi import FastAPI
import joblib
import pandas as pd
from app.schemas import LoanInput

app = FastAPI()

model = joblib.load("app/loan_pipeline_log.pkl")

@app.get("/")
def home():
    return {"message": "Loan Default Prediction API"}

@app.post("/predict")
def predict(data: LoanInput):

    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df)

    return {
        "prediction": int(prediction[0])
    }
