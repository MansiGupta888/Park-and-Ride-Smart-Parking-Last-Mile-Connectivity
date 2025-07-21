# backend/services/booking_service.py

from datetime import datetime, timedelta

# In-memory mock store; you can replace this with a real DB connection
booked_slots = []

def check_slot_availability(location: str) -> bool:
    # Example rule: max 5 bookings per location
    count = sum(1 for b in booked_slots if b['location'] == location)
    return count < 5

def reserve_slot(data: dict) -> dict:
    if not check_slot_availability(data['location']):
        return {"success": False, "message": "No slots available"}

    booking_id = f"BKG-{len(booked_slots) + 1:03d}"
    booking_data = {
        "id": booking_id,
        "user_email": data["user_email"],
        "location": data["location"],
        "duration": data["duration"],
        "timestamp": datetime.utcnow()
    }
    booked_slots.append(booking_data)
    return {"success": True, "booking": booking_data}

def cleanup_old_bookings(hours: int = 24):
    cutoff = datetime.utcnow() - timedelta(hours=hours)
    global booked_slots
    booked_slots = [b for b in booked_slots if b["timestamp"] > cutoff]
