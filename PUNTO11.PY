print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
import math

# Función para calcular la distancia entre dos puntos
def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Solicitar las coordenadas del primer punto
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))

# Solicitar las coordenadas del segundo punto
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Calcular la distancia
distancia = calcular_distancia(x1, y1, x2, y2)

# Mostrar el resultado
print(f"La distancia entre los puntos es: {distancia:.2f}")
