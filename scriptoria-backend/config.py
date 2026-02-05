import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("AIzaSyA0dJsB-s7c3CiCQKBTC1zjLOR4qgfz7hg")
    DATA_PATH = "data/sessions"
