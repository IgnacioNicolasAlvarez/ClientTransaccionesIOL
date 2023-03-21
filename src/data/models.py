from typing import Union
from datetime import date, datetime, timezone
from pydantic import BaseModel, validator


class Order(BaseModel):
    numero: int
    fechaOrden: Union[str, date]
    tipo: str
    estado: str
    mercado: str
    simbolo: str
    cantidad: float
    monto: float
    modalidad: str
    precio: float
    fechaOperada: Union[str, date]
    cantidadOperada: float
    precioOperado: float
    montoOperado: float
    plazo: str

    @validator("numero")
    def validate_numero(cls, numero):
        if not isinstance(numero, int):
            raise ValueError("El número debe ser un entero.")
        return numero


    @validator("fechaOrden", "fechaOperada")
    def validate_fecha(cls, fecha):
        if isinstance(fecha, str):
            try:
                fecha = datetime.fromisoformat(fecha).replace(tzinfo=timezone.utc).date()
            except ValueError:
                fecha = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%f").date()
        elif not isinstance(fecha, date):
            raise ValueError(
                "La fecha debe ser una cadena en formato ISO o un objeto date."
            )
        return fecha

    @validator("tipo")
    def validate_tipo(cls, tipo):
        if tipo not in ["Compra", "Venta"]:
            raise ValueError("El tipo debe ser 'Compra' o 'Venta'.")
        return tipo

    @validator("estado")
    def validate_estado(cls, estado):
        if estado not in ["pendiente", "terminada", "cancelada"]:
            raise ValueError(
                "El estado debe ser 'pendiente', 'terminada' o 'cancelada'."
            )
        return estado

    @validator("mercado", "simbolo")
    def validate_not_empty(cls, value):
        if not value:
            raise ValueError("Este campo es obligatorio.")
        return value

    @validator("cantidad", "cantidadOperada", pre=True)
    def parse_float(cls, value):
        return float(value)

    @validator("monto", "montoOperado", pre=True)
    def parse_float_or_none(cls, value):
        if value is not None:
            return float(value)
        else:
            return None

    @validator("precio", "precioOperado", pre=True)
    def parse_float_or_zero(cls, value):
        if value is None:
            return 0.0
        else:
            return float(value)
