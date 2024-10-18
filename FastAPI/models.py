from database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean


class Transactions(Base):
    
    __tablename__= 'transactions'
    
    id =   Column(Integer, primarykey=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)
    
