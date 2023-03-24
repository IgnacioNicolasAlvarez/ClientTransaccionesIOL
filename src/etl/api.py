from prefect import task

from config import settings
from src import logger
from src.api.auth import login
from src.api.client import get_operaciones
from src.data.database import OrderRepository
from src.data.models import Order


@task(retries=2, retry_delay_seconds=60)
def task_consume_api() -> list:
    token = login(
        password=settings.iol.credentials.password,
        username=settings.iol.credentials.username,
        url=settings.api.urls.login,
    )

    if token:
        database = OrderRepository.get_instance()
        last_fechaOrden = database.get_last_date()

        if last_fechaOrden:
            operaciones_raw = get_operaciones(fecha_desde=last_fechaOrden, token=token)
        else:
            operaciones_raw = get_operaciones(
                fecha_desde=settings.execution.start_date, token=token
            )

    else:
        logger.info("Login failed")

    return operaciones_raw


@task
def task_transform(raw: list) -> list:
    orders = [Order(**item) for item in raw]
    return orders


@task
def task_load(orders: list) -> None:
    database = OrderRepository.get_instance()
    database.delete_last_loaded_orders()

    for order in orders:
        database.create(order)
