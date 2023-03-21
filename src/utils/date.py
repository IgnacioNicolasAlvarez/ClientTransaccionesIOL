def es_dia_habil(fecha):
    """
    Devuelve True si la fecha es un día hábil (de lunes a viernes), False de lo contrario.
    """
    return fecha.weekday() < 5
