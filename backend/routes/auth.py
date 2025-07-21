# backend/routes/auth.py
from fastapi import APIRouter, HTTPException
from models.user import User, UserLogin
from passlib.hash import bcrypt
from jose import jwt
import os

router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY", "SECRET")

fake_user_db = {}  # Replace with MongoDB query

@router.post("/register")
def register(user: User):
    if user.email in fake_user_db:
        raise HTTPException(status_code=400, detail="User exists")
    hashed = bcrypt.hash(user.password)
    fake_user_db[user.email] = {"email": user.email, "password": hashed}
    return {"msg": "Registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = fake_user_db.get(user.email)
    if not db_user or not bcrypt.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"email": user.email}, SECRET_KEY)
    return {"access_token": token}
