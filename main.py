# fastapi uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from .chain import generate_response
import joblib 

model = joblib.load(r"D:\GenerativeAI\GenAI\LLM-Applications\Backend\SLR.joblib")

app = FastAPI(title = "LLM-Based-Application")

class User_input(BaseModel):
    message : str

class PredictInput(BaseModel):
    year: float


@app.get("/")
def home():
    return {"message" : "Hello, LLM-Based-Application"}

@app.post("/chat")
def response(user_input: User_input):
    result = generate_response(user_input.message)
    return {"result" : result}

@app.post("/predict")
def predict(user_input: PredictInput):
    prediction = model.predict([[user_input.year]])

    # Convert numpy type to Python native type
    salary = float(prediction[0])

    return {"salary": salary}