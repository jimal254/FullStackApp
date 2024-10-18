from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, sessionlocal
import models

app = FastAPI()

origin =[
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
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
        
        
db_depends = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"hello": "world"}

@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(transaction:TransactionBase, db:db_depends):
    db_transaction = models.Transactions(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
    
@app.get("/transactions", response_model=List[TransactionModel])
async def read_transaction(db:db_depends, skip:int = 0, limit:int = 100):
    transactions = db.query(models.Transactions).offset(skip).limit(limit).all()
    return transactions
