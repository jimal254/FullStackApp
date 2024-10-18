from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlachemy.ext.declarative import declarative_base


URL_DB = 'postgresql://postgres:123@localhost:5432/project'

engine = create_engine(URL_DB, connect_args={"check_same_thread: False"})

sessionlocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative_base()

