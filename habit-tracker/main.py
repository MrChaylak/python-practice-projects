import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("C:/PyNotes/.env")
USERNAME = os.getenv("MyPixelaName")
TOKEN = os.getenv("MyPixelaToken")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "h",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

graph_update = {
    "timezone": "Europe/Istanbul"
}

# response = requests.put(url=pixel_endpoint, json=graph_update, headers=headers)
# print(response.text)

