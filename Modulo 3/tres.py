# tres.py

# Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán 
# a medida que entren en la atmósfera de la Tierra.

# Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros 
# golpeara la Tierra, causaría mucho daño.

# También discutimos en el ejercicio anterior que:

# La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad 
# superior a 25 kilómetros por segundo (km/s) merece una advertencia. 
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, 
# a veces produce un rayo de luz que se puede ver desde la Tierra.

# Usando toda esta información, escribe un programa que emita la advertencia o información correcta 
# a la gente de la Tierra, según la velocidad y el tamaño de un asteroide. Utiliza instrucciones 
# if, else, y elif, así como los operadores and y or.

# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar 
# qué mensaje se debe enviar a Tierra.


asteroide_tam = 30
asteroide_vel = 19
if asteroide_tam >= 1000:
    print("¡Todo se termino! X|")
elif asteroide_vel > 25 or (asteroide_tam > 25 and asteroide_tam < 1000):
    print("¡Cuidado!¡Un asteroide peligroso se acerca! :o")
elif asteroide_vel >= 20 or asteroide_tam <= 25:
    print("¡Busca, busca! En el cielo se ve un destello de luz")
else:
    print("¡Todo tranquilo! ¡Nada que ver! (TT)")