from datetime import datetime
from pydantic import BaseModel, validator


class FechaPydantic(BaseModel):
    fecha: str

    @validator("fecha")
    def validate_fecha(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Fecha debe ser en formato YYYY-MM-DD")
        return v
