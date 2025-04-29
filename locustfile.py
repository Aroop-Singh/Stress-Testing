# locustfile.py
import random
from locust import HttpUser, task, between

PAYMENT_METHODS = ["VISA", "MasterCard", "Amex", "Discover"]

class FlightBookingUser(HttpUser):
    wait_time = between(1, 3)   # each user waits 1–3s between tasks

    @task
    def book_flight(self):
        payload = {
            "user_id": random.randint(1, 10_000),
            "flight_id": random.randint(1000, 9999),
            "payment_method": random.choice(PAYMENT_METHODS)
        }
        self.client.post("/api/book", json=payload)
