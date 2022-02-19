# throw.py

from typing import Type


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # Si el argumento es entero, la siguiente opreacion funcionara
            argument / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben ser de tipo entero, pero se recibio: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronauts} astronautas despues de {days_left} dias!")
    return f"Agua total que queda después de {days_left} días es: {total_water_left} litros"

try:
    print(water_left("3", "200", None))
except RuntimeError as err:
    print(err)
except TypeError as err:
    print(err)