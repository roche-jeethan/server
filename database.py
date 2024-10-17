from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_database = 'mysql+pymysql://root:MySQL123456!@localhost:3306/techpirates'

engine = create_engine(URL_database)  # connect to server

SessionLocal =sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()