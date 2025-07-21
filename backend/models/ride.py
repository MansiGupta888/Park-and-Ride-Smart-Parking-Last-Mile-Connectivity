# backend/models/ride.py

from pydantic import BaseModel
from typing import Optional

class RideRequest(BaseModel):
    user_email: str
    pickup_location: str
    drop_location: str
    ride_type: str  # cab / e-rickshaw / shuttle

class RideOption(BaseModel):
    name: str
    capacity: int
    price_per_km: float
    wait_time_min: int
