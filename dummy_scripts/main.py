import requests
import random
from datetime import datetime

# Replace this with the actual URL of your API
API_URL = "http://localhost:8000/charts/api/data/"


def get_dummy_data(node, packet_number):
    dummy_data = {
        "packet_number": packet_number,
        "node": node,
        "temperature": round(random.uniform(20, 30), 1),
        "light": random.randint(0, 100),
        "humidity": random.randint(0, 100),
    }
    return dummy_data


for i in range(100):
    # Send the POST request
    dummy_data = get_dummy_data(22, i)
    response = requests.post(API_URL, json=dummy_data)

    # Check the response
    if response.status_code == 201:
        print("Data posted successfully.")
        print("Response:", response.json())
    else:
        print("Failed to post data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
