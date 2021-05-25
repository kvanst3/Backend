import requests
import os


USERNAME = 'indiko'
TOKEN = os.environ.get('D_KEY')


# Create account

pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token": TOKEN,
    "username": "indikool",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=params)
# print(response.text)


# Create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

params = {
    "id": "graph0",
    "name": "Coding",
    "unit": "hours",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=params, headers=headers)
# print(response.text)


# Add to graph