import pickle

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


with open('catboost.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()


class Titanic(BaseModel):
    Pclass: int
    Sex: str
    Age: float


@app.post('/predict')
def predict(data: Titanic):
    data_to_predict = np.array([[data.Pclass, data.Sex, data.Age]])
    prediction = model.predict(data_to_predict)
    return {"prediction": int(prediction[0])}
