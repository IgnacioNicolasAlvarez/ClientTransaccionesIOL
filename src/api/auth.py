import requests


def login(username: str, password: str, url: str) -> str:
    credentials = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url, data=credentials, headers=headers)
    if response.status_code == 200:
        out_json = response.json()
        token = f"{out_json['token_type']} {out_json['access_token']}"
        return token
    else:
        return None
