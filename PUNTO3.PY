print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
def factorial(n):
    
    #Calcula el factorial de un número positivo.
    
    if n < 0:
        return "Número no válido"
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
print(factorial(5)) 
