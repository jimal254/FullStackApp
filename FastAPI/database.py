from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


URL_DB = 'postgresql://postgres:123@localhost:5432/project'

engine = create_engine(URL_DB)

sessionlocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)

Base = declarative_base()
