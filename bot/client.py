import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = "https://testnet.binancefuture.com"


# 🔐 Generate signature
def generate_signature(query_string):
    return hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()


# 🕒 Get Binance server time (FIX FOR ERROR -1021)
def get_server_time():
    url = f"{BASE_URL}/fapi/v1/time"
    response = requests.get(url)
    return response.json()['serverTime']


# 🔁 Send signed request (for private endpoints)
def send_signed_request(method, endpoint, params=None):
    if params is None:
        params = {}

    # ✅ Use Binance server time instead of local time
    params['timestamp'] = get_server_time()

    # Convert params to query string
    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])

    # Generate signature
    signature = generate_signature(query_string)

    # Final URL
    url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.request(method, url, headers=headers)

    return response.json()


# 🌐 Public request (no auth)
def send_public_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    return response.json()