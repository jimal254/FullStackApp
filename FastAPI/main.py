from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from sqlalchemy.orm import session
from pydantic import BaseModel
from database import session, engine, sessionlocal
import models

app = FastAPI()

origin =[
    'http://localhost:3000'
]

app.middleware(
    CORSMiddleware,
    allow_origins=origin, 
)


#validate req from react app
class TransactionBase(BaseModel):
    amount:float
    category:str
    description:str
    is_income:bool
    date:str
     
class TransactionModel(TransactionBase):
    id:int

    class Config:
        orm_mode = True
        
def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"hello": "world"}