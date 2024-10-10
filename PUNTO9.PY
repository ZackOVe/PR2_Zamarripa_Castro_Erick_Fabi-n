print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
def suma(numeros):
    
    #Suma todos los números de una lista.

    total = 0
    for numero in numeros:
        total += numero
    return total

def multiplicar(numeros):
    
    #Multiplica todos los números de una lista.
    
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado
print("Los resultados son: ")
print(suma([16, 22, 13, 9]))  
print(multiplicar([17, 28, 20, 14])) 
