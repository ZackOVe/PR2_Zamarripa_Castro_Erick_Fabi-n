print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")

import math

def area_circulo(radio):
    
    #Calcula el área de un círculo.

    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):

    #Calcula el volumen de un cilindro.
    
    area = area_circulo(radio)
    return area * altura

# Ejemplo de uso
print(area_circulo(5))  
print(volumen_cilindro(5, 10))  
