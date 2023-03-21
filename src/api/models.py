from datetime import datetime
from pydantic import BaseModel, validator


class FechaPydantic(BaseModel):
    fecha: datetime

    @validator("fecha", pre=True)
    def validate_fecha(cls, v):
        if isinstance(v, datetime):
            return v
        elif isinstance(v, str):
            try:
                return datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                pass
        raise ValueError("Fecha debe ser en formato (YYYY-MM-DD HH:MM:SS)")
