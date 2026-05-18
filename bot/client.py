import os 
from binance import Client
from dotenv import load_dotenv
load_dotenv()

def get_client():
    api_key = os.getenv('api_key')
    api_secret = os.getenv('secret_key')

    if api_key is None or api_secret is None:
        raise ValueError("API key and secret key must be set in the environment variables.")
    
    
    client = Client(
        api_key,
        api_secret,
        testnet=True,
        base_endpoint="https://demo-fapi.binance.com"
    )
    return client