from typing import List

import psycopg2

from config import settings
from src.data.models import Order


class OrderRepository:
    instance = None

    @staticmethod
    def get_instance():
        if not OrderRepository.instance:
            OrderRepository.instance = OrderRepository()
        return OrderRepository.instance

    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.db.credentials.POSTGRES_HOST,
            database=settings.db.credentials.POSTGRES_DB,
            user=settings.db.credentials.POSTGRES_USER,
            password=settings.db.credentials.POSTGRES_PASSWORD,
        )
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS orders (numero INTEGER, fechaOrden TIMESTAMP, tipo TEXT, estado TEXT, mercado TEXT, simbolo TEXT, cantidad FLOAT, monto FLOAT, modalidad TEXT, precio FLOAT, fechaOperada TIMESTAMP, cantidadOperada FLOAT, precioOperado FLOAT, montoOperado FLOAT, plazo TEXT)"
        )

    def create(self, order: Order) -> int:
        query = f"INSERT INTO orders (numero, fechaOrden, tipo, estado, mercado, simbolo, cantidad, monto, modalidad, precio, fechaOperada, cantidadOperada, precioOperado, montoOperado, plazo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            order.numero,
            order.fechaOrden,
            order.tipo,
            order.estado,
            order.mercado,
            order.simbolo,
            order.cantidad,
            order.monto,
            order.modalidad,
            order.precio,
            order.fechaOperada,
            order.cantidadOperada,
            order.precioOperado,
            order.montoOperado,
            order.plazo,
        )
        self.cur.execute(query, values)
        self.conn.commit()
        return self.cur.rowcount

    def get_by_numero(self, numero: int) -> Order:
        query = f"SELECT * FROM orders WHERE numero = {numero}"
        self.cur.execute(query)
        row = self.cur.fetchone()
        if row:
            return Order(*row)
        else:
            return None

    def get_all(self) -> List[Order]:
        query = "SELECT * FROM orders"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        orders = [Order(*row) for row in rows]
        return orders

    def get_last_date(self) -> str:
        query = "SELECT fechaOrden FROM orders ORDER BY fechaOrden DESC LIMIT 1"
        self.cur.execute(query)
        row = self.cur.fetchone()
        if row:
            return row[0]
        else:
            return None

    def delete_last_loaded_orders(self):
        last_date = self.get_last_date()
        if last_date is not None:
            last_loaded_date = last_date.date().isoformat()
            query = f"DELETE FROM orders WHERE fechaOrden::date = '{last_loaded_date}'"
            self.cur.execute(query)
            self.conn.commit()
