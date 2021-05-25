import requests
import os


USERNAME = 'indiko'
TOKEN = os.environ.get('D_KEY')
GRAPH_ID = "graph0"


# Create account

base_endpoint = "https://pixe.la/v1/users"
params = {
    "token": TOKEN,
    "username": "indikool",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=params)
# print(response.text)


# Create graph

graph_endpoint = f"{base_endpoint}/{USERNAME}/graphs"

params = {
    "id": GRAPH_ID,
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

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

params = {
    "date": "20210525",
    "quantity": "3",
}

response = requests.post(pixel_endpoint, json=params, headers=headers)
print(response.text)
