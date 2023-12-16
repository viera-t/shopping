from fastapi import FastAPI
import api.shoppingtrends as shopping
import api.shopping_view as shopping_view
import api.shopping_train as shopping_train

app = FastAPI()
app.include_router(shopping.router)
app.include_router(shopping_view.router)
app.include_router(shopping_train.router)

@app.get("/")
async def root():
    return {"message": "Hello"}





