from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()

fake_users = []

class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

@router.post("/signup")
def signup(user: SignupRequest):
    if any(u["email"] == user.email for u in fake_users):
        raise HTTPException(status_code=400, detail="Email already registered")
    fake_users.append(user.dict())
    return {"message": "Signup successful", "user": user.username}
