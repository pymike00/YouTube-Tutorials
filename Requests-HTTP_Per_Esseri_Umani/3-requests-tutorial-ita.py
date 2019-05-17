import requests

def login(credentials):
    """Date delle credenziali, effettua il login all'app
    e restituisci un token di autenticazione ricevuto dall'app.
    """
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    if response.ok:
        print("Login: Success!")
        print(response.json())
        auth_token = response.json()['key']
        return auth_token
    else:
        raise Exception("Errore. ", response.status_code)

def auth_request(endpoint, auth_token):
    """Dato un endpoint e un token di autenticazione, 
    effettua una richiesta di tipo GET.
    """
    auth_header = f"Token { auth_token }"
    headers = {"Authorization": auth_header}

    response = requests.get(endpoint, headers=headers)

    if response.ok:
        response_data = response.json()
        print("Data: ", response_data)
    else:
        raise Exception("Errore. ", response.status_code)


if __name__ == "__main__":
    credentials = {"username": "", "password": ""}
    auth_token = login(credentials)
    endpoint = "http://127.0.0.1:8000/api/questions/"

    auth_request(endpoint, auth_token)
