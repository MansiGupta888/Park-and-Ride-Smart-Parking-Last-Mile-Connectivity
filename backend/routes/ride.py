# backend/routes/ride.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/options")
def ride_options():
    return ["cab", "e-rickshaw", "shuttle"]
