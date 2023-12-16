from pydantic import BaseModel

class ShoppingBase(BaseModel):

    Age: int
    Gender: str
    Item_Purchased: str
    Category: str
    Purchase_Amount_USD: int
    Location: str
    Size: str
    Color: str
    Season: str
    Review_Rating: int
    Subscription_Status: str
    Payment_Method: str
    Shipping_Type: str
    Discount_Applied: str
    Promo_Code_Used: str
    Previous_Purchases: int
    Preferred_Payment_Method: str
    Frequency_of_Purchases: str

#PREDICT

class ShoppingPredictBase(BaseModel):

    Customer_ID: int
    Age: int
    Review_Rating: int
    #Purchase_Amount_USD: int
    Previous_Purchases: int

class ShoppingCreate(ShoppingBase):
    pass

class ShoppingUpdate(ShoppingBase):
    pass

class Shopping(ShoppingBase):
    Customer_ID: int

    class Config:
        orm_mode = True