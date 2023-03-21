from datetime import date, datetime, timedelta
from src import logger
import requests

from config import settings
from .models import FechaPydantic
from src.utils.date import es_dia_habil


def get_operaciones(token, estado="terminadas", fecha_desde=None, fecha_hasta=None):
    if not token:
        raise ValueError("Not logged in")

    url = settings.api.urls.operaciones
    headers = {"Authorization": f"{token}"}

    if not fecha_hasta:
        fecha_hasta = FechaPydantic(fecha=datetime.today().strftime("%Y-%m-%d"))

    if not fecha_desde:
        fecha_desde = FechaPydantic(
            fecha=(
                date.today() - timedelta(days=1 if es_dia_habil(date.today()) else 3)
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
