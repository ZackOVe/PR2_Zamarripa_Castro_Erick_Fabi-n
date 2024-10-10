# PR2_Zamarripa_Castro_Erick_Fabi-n
Practica de varios puntos de 11 funciones de proposito variado

PUNTO #1}

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Define el saludo para luego imprimir el texto declarado

def mostrar_saludo():

print("Hey amigos!")
    
print("")

#Llamada a la función

mostrar_saludo()

PUNTO #2

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Definira el nombre para imprimirlo junto al texto ya ingresado

def saludar(nombre):

  print(f"¡Hola {nombre}!")

#Ejemplo

saludar("Fabián")

PUNTO #3

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
    
   resultado *= 1
   
return resultado
    

# Ejemplo de uso

print(factorial(5))  # Salida: 120

PUNTO #4}

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def calcular_factura(sin_iva, iva=21):
    
  #Calcula el total de una factura incluyendo IVA.
    
  total = sin_iva * (1 + iva / 100)
 return total

# Ejemplo de uso

print(calcular_factura(100))  # Salida: 121.0

PUNTO #5

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

print(area_circulo(5))  # Salida: 78.54

print(volumen_cilindro(5, 10))  # Salida: 392.70

PUNTO #6

print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")
def validar_email(email):
    
 #Verifica si un email es válido (contiene '@').    
 return '@' in email

# Ejemplo de uso
print(validar_email("usuario@ejemplo.com"))  # Salida: True


