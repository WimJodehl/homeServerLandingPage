import os

class Config:
    SECRET_KEY = os.urandom(24)  # Use a secure, randomly generated secret key
