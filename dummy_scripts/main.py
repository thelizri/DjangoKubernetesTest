import requests
import random
from datetime import datetime
from time import sleep

# Replace this with the actual URL of your API
API_URL = "http://william.discworld.cc/charts/api/data/"


def get_dummy_data(packet_number):
    dummy_data = {
        "packet_number": packet_number,
        "node": -1,
        "temperature": 70,
        "light": 160,
        "humidity": 26,
    }
    return dummy_data


for i in range(20):
    # Send the POST request
    dummy_data = get_dummy_data(i)
    response = requests.post(API_URL, json=dummy_data)

    # Check the response
    if response.status_code == 201:
        print("Data posted successfully.")
        print("Response:", response.json())
    else:
        print("Failed to post data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

    sleep(3)
