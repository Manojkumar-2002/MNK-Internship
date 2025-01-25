from datetime import datetime

import requests

PIXEL_ENDPOINT = "https://pixe.la/v1"

CREATE_USER_END_POINT = f"{PIXEL_ENDPOINT}/users/"

GRAPH_ID = "graph1"
TOKEN = "1234abCD"
USER_NAME = "manoj"

user_config = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

user_res = requests.post(CREATE_USER_END_POINT,json=user_config)
print(user_res.text)

GRAPH_END_POINT = f"{PIXEL_ENDPOINT}/users/{USER_NAME}/graphs/"

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name":"First Graph",
    "unit":"km",
    "type":"float",
    "color":"shibafu"
}

graph_res = requests.post(GRAPH_END_POINT,json=graph_config,headers=headers)
print(graph_res.text)