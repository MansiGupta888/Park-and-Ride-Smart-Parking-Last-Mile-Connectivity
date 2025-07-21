# backend/routes/booking.py
from fastapi import APIRouter
from models.booking import Booking
import uuid
from datetime import datetime

router = APIRouter()
bookings = []

@router.post("/reserve")
def reserve(booking: Booking):
    booking.id = str(uuid.uuid4())
    booking.timestamp = datetime.utcnow()
    bookings.append(booking)
    return {"msg": "Booking confirmed", "booking_id": booking.id}
