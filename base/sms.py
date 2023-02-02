import requests
import random
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(100000, 999999)
        url = "https://smspoh.com/api/v2/send"
        # requests.post(url, headers={"Authorization":os.environ['APIKEY']},
        # json={"to":phone_number, "message":"Your verificatin code is "+otp, "sender":"hello"})
        return otp
    except Exception as e:
        return None
