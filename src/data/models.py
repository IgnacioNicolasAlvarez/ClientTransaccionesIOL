from datetime import datetime, timezone
from typing import Union

from pydantic import BaseModel, validator


class Order(BaseModel):
    numero: int
    fechaOrden: Union[str, datetime]
    tipo: str
    estado: str
    mercado: str
    simbolo: str
    cantidad: float
    monto: float
    modalidad: str
    precio: float
    fechaOperada: Union[str, datetime]
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
                fecha = datetime.fromisoformat(fecha).replace(tzinfo=timezone.utc)
            except ValueError:
                fecha = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.%f")
        elif not isinstance(fecha, datetime):
            raise ValueError(
                "La fecha debe ser una cadena en formato ISO o un objeto datetime."
            )
        return fecha

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

    @validator(
        "cantidad",
        "cantidadOperada",
        "monto",
        "montoOperado",
        "precio",
        "precioOperado",
        pre=True,
    )
    def parse_float(cls, value):
        if value is None:
            return 0.0
        else:
            return float(value)
