from config import settings
from src.api.auth import login
from src.api.client import get_operaciones
from src import logger
from src.data.models import Order
from src.data.database import OrderRepository


def task_consume_api() -> list:
    token = login(
        password=settings.iol.credentials.password,
        username=settings.iol.credentials.username,
        url=settings.api.urls.login,
    )

    if token:
        operaciones_raw = get_operaciones(fecha_desde="2021-01-01", token=token)

    else:
        logger.info("Login failed")

    return operaciones_raw


def task_transform(raw: list):
    orders = [Order(**item) for item in raw if item["tipo"] in ["Compra", "Venta"]]

    database = OrderRepository(db_file="order.db")

    for order in orders:
        if order.tipo in ["Compra", "Venta"]:
            database.create(order)
