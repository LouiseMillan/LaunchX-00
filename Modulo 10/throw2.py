# throw.py

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronauts} astronautas despues de {days_left} dias!")
    return f"Agua total que queda después de {days_left} días es: {total_water_left} litros"

try:
    print(water_left(5, 100, 2))
except RuntimeError as err:
    print(err)