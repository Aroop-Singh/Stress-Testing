from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Booking(BaseModel):
    user_id: int
    flight_id: int
    payment_method: str

@app.post("/api/book")
def book_flight(booking: Booking):
    return {"message": "Booking received!"}
