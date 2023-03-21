from datetime import datetime, timedelta, date

import requests

from src.model.iol import FechaPydantic
from config import settings


def es_dia_habil(fecha):
    """
    Devuelve True si la fecha es un día hábil (de lunes a viernes), False de lo contrario.
    """
    return fecha.weekday() < 5


class IOL:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = settings.api.urls.login
        self.token = None

    def login(self):
        credentials = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(self.url, data=credentials, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            self.token = (
                f"{response_json['token_type']} {response_json['access_token']}"
            )
            return True
        else:
            return False

    def get_operaciones(self, estado="terminadas", fecha_desde=None, fecha_hasta=None):
        if not self.token:
            raise ValueError("Not logged in")

        url = settings.api.urls.operaciones
        headers = {"Authorization": f"{self.token}"}

        if not fecha_hasta:
            fecha_hasta = FechaPydantic(fecha=datetime.today().strftime("%Y-%m-%d"))

        if not fecha_desde:
            fecha_desde = FechaPydantic(
                fecha=(
                    date.today()
                    - timedelta(days=1 if es_dia_habil(date.today()) else 3)
                ).strftime("%Y-%m-%d")
            )
        elif isinstance(fecha_desde, FechaPydantic):
            fecha_desde = fecha_desde
        else:
            fecha_desde = FechaPydantic(fecha=fecha_desde)

        params = {
            "estado": estado,
            "fechaDesde": fecha_desde.fecha,
            "fechaHasta": fecha_hasta.fecha,
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None
