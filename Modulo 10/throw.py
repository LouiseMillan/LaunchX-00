# throw.py

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Agua total que queda después de {days_left} días es: {total_water_left} litros"

print(water_left(5, 100, 2))
