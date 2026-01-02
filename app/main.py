from fastapi import FastAPI
from datetime import datetime
from app.routes import (users_router, prompts_router,favourites_router,login_router)
from fastapi.middleware.cors import CORSMiddleware
from uuid import UUID

app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


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
app.include_router(login_router,prefix="/auth",tags=["Login_Authentication"])
