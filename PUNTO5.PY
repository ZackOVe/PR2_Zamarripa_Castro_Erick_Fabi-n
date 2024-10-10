print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")

import math

#Función para calcular el área de un círculo

def area_circulo(radio):
    return math.pi * (radio ** 2)

#Función para calcular el volumen de un cilindro

def volumen_cilindro(radio, altura):
    area = area_circulo(radio)
    return area * altura

#Solicitar el radio para el círculo

radio = float(input("Ingrese el radio del círculo: "))
area = area_circulo(radio)
print(f"El área del círculo es: {area:.2f}")

#Solicitar el radio y la altura del cilindro

altura = float(input("Ingrese la altura del cilindro: "))
volumen = volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen:.2f}")
