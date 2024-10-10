print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
def distancia_dos_puntos(punto1, punto2):
    
    #Calcula la distancia entre dos puntos.
    
    x1, y1 = punto1
    x2, y2 = punto2
    return (x2 - x1, y2 - y1)

# Ejemplo de uso
print(distancia_dos_puntos((1, 2), (4, 6)))