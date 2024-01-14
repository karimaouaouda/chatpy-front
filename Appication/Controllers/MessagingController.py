import json
import requests


def send(message):
    url = 'http://localhost:8000/send'
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(message)
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response)
        return response
    else:
        return None
