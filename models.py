from sqlalchemy import Column,String 
from database import Base

class User(Base):
    __tablename__ = 'techpirates'

    user_name = Column(String(50), primary_key=True, index=True)
    password = Column(String(128))
    contact = Column(String(10))