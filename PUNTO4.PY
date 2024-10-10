print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
def calcular_factura(sin_iva, iva=21):
    
    #Calcula el total de una factura incluyendo IVA.
    
    total = sin_iva * (1 + iva / 100)
    return total

# Ejemplo de uso
print(calcular_factura(100))  
