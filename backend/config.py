# backend/config.py
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "SECRET")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
