# uno.py

# Para este ejercicio, escribirás una lógica condicional que imprima una advertencia si 
# un asteroide se acerca a la Tierra demasiado rápido. La velocidad del asteroide varía 
# dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros
# por segundo (km/s) merece una advertencia.

# Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

asteroide_vel = 49
if asteroide_vel > 25:
    print("¡Cuidado!¡Un asteroide se acerca desasiado rápido! :o")
else:
    print("¡Todo tranquilo!")