from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
import bcrypt
from database import SessionLocal, engine

# Creating a FastAPI instance
app = FastAPI()

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Pydantic schema for request validation
class UserCreate(BaseModel):
    user_name: str
    password: str
    contact: str

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Hashing function using bcrypt
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')    

@app.post("/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Hash the password before storing it
    hashed_password = hash_password(user_data.password)

    # Create a new user model instance
    new_user = models.User(
        user_name=user_data.user_name,
        password=hashed_password,  # Use the hashed password
        contact=user_data.contact
    )

    # Add the new user to the session and commit it to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return a success message
    return {
        "message": "User created successfully!",
        "user_data": {
            "user_name": user_data.user_name,
            "contact": user_data.contact
        }
    }
