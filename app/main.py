from fastapi import FastAPI
from app.api import time_tracking, hrm

app = FastAPI()

app.include_router(time_tracking.router, prefix="/time-tracking", tags=["Time Tracking"])
app.include_router(hrm.router, prefix="/hrm", tags=["HRM"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Time Tracking and HRM API"}