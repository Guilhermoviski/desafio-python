from dotenv import load_dotenv
from supabase import create_client
import os
import requests

load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

ID_INSTANCIA = os.getenv("ZAPI_ID")
ID_TOKEN = os.getenv("ZAPI_TOKEN")
ID_CLIENTE_TOKEN = os.getenv("ZAPI_CLIENTE_TOKEN")

url_zapi = f"https://api.z-api.io/instances/{ID_INSTANCIA}/token/{ID_TOKEN}/send-text"