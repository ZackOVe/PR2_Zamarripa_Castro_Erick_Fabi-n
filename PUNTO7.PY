print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
def longitud_ultima_palabra(texto):
    
    #Devuelve la longitud de la última palabra.
   
    palabras = texto.split()
    if palabras:
        return len(palabras[-1])
    return 0

# Ejemplo de uso
print(longitud_ultima_palabra("Hola mundo"))  