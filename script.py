import os

import requests
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")


url = "https://graph.instagram.com/me"

params = {
    "fields": "user_id,username",
    "access_token": ACCESS_TOKEN
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)
print("Response:")
print(response.json())