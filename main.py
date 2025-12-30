from fastapi import FastAPI
from datetime import datetime
from api.routes import (users_router, prompts_router,favourites_router)
from dotenv import load_dotenv
import os


app = FastAPI()

print(os.getenv("SUPABASE_URL"))
print(os.getenv("SUPABASE_KEY"))


@app.get("/")
def read_root():
    return {"status": "Working"}


users = [
    {
        "id": 1,
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@doe.com",
        "password": "john1234",
        "dateCreated": datetime.now()
    },
    {
        "id": 2,
        "firstName": "John",
        "lastName": "Lark",
        "email": "john@dolarke.com",
        "password": "john1234",
        "dateCreated": datetime.now()
    }
]

app.include_router(users_router, tags=["Users"])
app.include_router(prompts_router, tags=["Prompts"])
app.include_router(favourites_router, tags=["Favourites"])
