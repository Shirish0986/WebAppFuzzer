# config.py
import os

TIMEOUT = int(os.getenv("TIMEOUT", 10))
RETRIES = int(os.getenv("RETRIES", 3))
