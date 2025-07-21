
# backend/models/booking.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Booking(BaseModel):
    user_email: str
    location: str
    duration: str  # hourly/daily/monthly
    timestamp: Optional[datetime] = None
    id: Optional[str] = None
