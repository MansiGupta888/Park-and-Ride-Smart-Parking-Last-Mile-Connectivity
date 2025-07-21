from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import auth, booking, ride
from database.connection import connect_to_mongo

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve favicon
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Park & Ride API"}

# MongoDB startup
@app.on_event("startup")
async def startup():
    await connect_to_mongo()

# Routers
app.include_router(auth.router, prefix="/auth")
app.include_router(booking.router, prefix="/booking")
app.include_router(ride.router, prefix="/ride")
