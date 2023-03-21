import duckdb
from typing import List
from src.data.models import Order


class OrderRepository:
    instance = None

    @staticmethod
    def get_instance(db_file: str) -> "OrderRepository":
        if not OrderRepository.instance:
            OrderRepository.instance = OrderRepository(db_file)
        return OrderRepository.instance
    
    def __init__(self, db_file: str):
        self.conn = duckdb.connect(db_file)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS orders (numero INTEGER, fechaOrden DATETIME, tipo TEXT, estado TEXT, mercado TEXT, simbolo TEXT, cantidad FLOAT, monto FLOAT, modalidad TEXT, precio FLOAT, fechaOperada DATETIME, cantidadOperada FLOAT, precioOperado FLOAT, montoOperado FLOAT, plazo TEXT)"
        )

    def create(self, order: Order) -> int:
        query = f"INSERT INTO orders (numero, fechaOrden, tipo, estado, mercado, simbolo, cantidad, monto, modalidad, precio, fechaOperada, cantidadOperada, precioOperado, montoOperado, plazo) VALUES ({order.numero}, '{order.fechaOrden}', '{order.tipo}', '{order.estado}', '{order.mercado}', '{order.simbolo}', {order.cantidad}, {order.monto}, '{order.modalidad}', {order.precio}, '{order.fechaOperada}', {order.cantidadOperada}, {order.precioOperado}, {order.montoOperado}, '{order.plazo}')"
        result = self.conn.execute(query)
        self.conn.commit()
        return result

    def get_by_numero(self, numero: int) -> Order:
        query = f"SELECT * FROM orders WHERE numero = {numero}"
        result = self.conn.execute(query)
        row = result.fetchone()
        if row:
            return Order(*row)
        else:
            return None

    def get_all(self) -> List[Order]:
        query = "SELECT * FROM orders"
        result = self.conn.execute(query)
        rows = result.fetchall()
        orders = [Order(*row) for row in rows]
        return orders

    def get_last_date(self) -> str:
        query = "SELECT fechaOrden FROM orders ORDER BY fechaOrden DESC LIMIT 1"
        result = self.conn.execute(query)
        row = result.fetchone()
        if row:
            return row[0]
        else:
            return None