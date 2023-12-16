from fastapi import APIRouter, HTTPException
from database import db_cursor, db_connection
#from models.shopping import Shopping, ShoppingCreate, ShoppingUpdate

from models.shoppingtrends import Shopping, ShoppingCreate, ShoppingUpdate

router = APIRouter()
@router.get("/shopping/", response_model=list[Shopping])
def read_all_shopping():
    query = "SELECT * FROM shopping_trends order by Customer_ID desc limit 20"
    db_cursor.execute(query)
    rows = db_cursor.fetchall()

    shopping = []
    column_names = [column[0] for column in db_cursor.description]
    for row in rows:
        shopping_dict = dict(zip(column_names, row))
        shopping.append(Shopping(**shopping_dict))

    return shopping

@router.get("/shopping/{data_id}", response_model=Shopping)
def read_shopping(data_id: int):
    query = "SELECT * FROM shopping_trends WHERE Customer_ID = %s"
    db_cursor.execute(query, (data_id,))
    row = db_cursor.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Data not found")

    shopping_dict = dict(zip(db_cursor.column_names, row))
    return Shopping(**shopping_dict)

@router.post("/shopping/", response_model=Shopping)
def create_shopping(data: ShoppingCreate):
    query = """
    INSERT INTO shopping_trends(Age,Gender,Item_Purchased,Category,Purchase_Amount_USD,Location,Size,Color,Season,Review_Rating,Subscription_Status,Payment_Method,Shipping_Type,Discount_Applied,Promo_Code_Used,Previous_Purchases,Preferred_Payment_Method,Frequency_of_Purchases) 
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """
    values = (
        data.Age, data.Gender, data.Item_Purchased , data.Category,
        data.Purchase_Amount_USD, data.Location, data.Size,
        data.Color, data.Season, data.Review_Rating,
        data.Subscription_Status, data.Payment_Method, data.Shipping_Type,
        data.Discount_Applied, data.Promo_Code_Used, data.Previous_Purchases,
        data.Preferred_Payment_Method, data.Frequency_of_Purchases
    )
    
    db_cursor.execute(query, values)
    db_connection.commit()
    
    shopping_id = db_cursor.lastrowid  # Get the auto-generated id
    return Shopping(Customer_ID=shopping_id, **data.dict())

@router.put("/shopping/{data_id}", response_model=Shopping)
def update_shopping(data_id: int, updated_data: ShoppingUpdate):
    query = """
    UPDATE shopping_trends
    SET Age = %s, Gender = %s, Item_Purchased = %s, Category = %s,
        Purchase_Amount_USD = %s, Location = %s, Size = %s,
        Color = %s, Season = %s, Review_Rating = %s,
        Subscription_Status = %s, Payment_Method = %s, Shipping_Type = %s,
        Discount_Applied = %s, Promo_Code_Used = %s, Previous_Purchases = %s,
        Preferred_Payment_Method = %s, Frequency_of_Purchases = %s
    WHERE Customer_ID = %s
    """
    values = (
        updated_data.Age, updated_data.Gender, updated_data.Item_Purchased,
        updated_data.Category, updated_data.Purchase_Amount_USD,
        updated_data.Location, updated_data.Size,
        updated_data.Color, updated_data.Season,
        updated_data.Review_Rating, updated_data.Subscription_Status,
        updated_data.Payment_Method, updated_data.Shipping_Type,
        updated_data.Discount_Applied, updated_data.Promo_Code_Used,
        updated_data.Previous_Purchases, updated_data.Preferred_Payment_Method,
        updated_data.Frequency_of_Purchases,
        data_id
    )
    
    db_cursor.execute(query, values)
    db_connection.commit()
    
    updated_data_dict = updated_data.dict()
    updated_data_dict["Customer_ID"] = data_id
    return Shopping(**updated_data_dict)

@router.delete("/shopping/{data_id}", response_model=Shopping)
def delete_shopping(data_id: int):
    query = "SELECT * FROM shopping_trends WHERE Customer_ID = %s"
    db_cursor.execute(query, (data_id,))
    row = db_cursor.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Data not found")
    
    deleted_shopping = dict(zip(db_cursor.column_names, row))
    
    delete_query = "DELETE FROM shopping_trends WHERE Customer_ID = %s"
    db_cursor.execute(delete_query, (data_id,))
    db_connection.commit()
    
    return deleted_shopping