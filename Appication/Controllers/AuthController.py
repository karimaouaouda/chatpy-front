import requests


class AuthController:
    def login(self, credentials):
        email = credentials['email']
        password = credentials['password']

        print(email, password)
        response = requests.post("http://127.0.0.1:8000/login", json={'email': email, 'password': password})

        if response.status_code == 200:
            return response.json()
        else:
            return False
