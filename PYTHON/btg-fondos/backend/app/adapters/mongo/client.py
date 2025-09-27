import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

def get_database():
    client = MongoClient(MONGO_URI)
    return client["btg_fondos"]  # 👈 asegúrate que el nombre es correcto
