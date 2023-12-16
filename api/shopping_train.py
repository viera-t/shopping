from fastapi import APIRouter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from database import db_cursor, db_connection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.metrics import r2_score
from models.shoppingtrends import ShoppingPredictBase
from fastapi import HTTPException
from pydantic import ValidationError

router = APIRouter()

@router.get("/shopping_model/train")
async def train():
    df = pd.read_sql("SELECT * FROM shopping_trends", con=db_connection)

    X = df.drop(["Purchase_Amount_USD"], axis="columns")
    y = df["Purchase_Amount_USD"]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    model_rf = RandomForestClassifier()
    model_rf.fit(X_train, y_train)

    with open('model_rf', 'wb') as files:
        pickle.dump(model_rf, files)

    yRF_predict = model_rf.predict(X_test)

    r2 = round(r2_score(y_test, yRF_predict), 3)

    return {"message": "model_rf", "R2": str(r2)}

@router.post("/shopping_model/predict")
async def predict(item: ShoppingPredictBase):
    try:
        df = pd.DataFrame(data={
            
            "Customer_ID": [item.Customer_ID],
            "Age": [item.Age],
            "Review_Rating": [item.Review_Rating],
            "Previous_Purchases": [item.Previous_Purchases]
        })


        with open('model_rf', 'rb') as f:
            lr = pickle.load(f)

        deploy_Y = lr.predict(df)
        deploy_arr = deploy_Y.tolist()

        prediction = int(deploy_arr[0])
        return {"Purchase_Amount_USD": prediction}

    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
