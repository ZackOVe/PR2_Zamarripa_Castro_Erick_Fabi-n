# PR2_Zamarripa_Castro_Erick_Fabi-n
Practica de varios puntos de 11 funciones de proposito variado

PUNTO #1

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Define el saludo para luego imprimir el texto declarado

def mostrar_saludo():

print("Hey amigos!")
    
print("")

#Llamada a la función

mostrar_saludo()

![image](https://github.com/user-attachments/assets/0b0d9c7b-8936-4ac4-96d6-542d27a485c4)

![image](https://github.com/user-attachments/assets/d7141384-4aed-4547-b557-764f42b58842)

PUNTO #2

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Definira el nombre para imprimirlo junto al texto ya ingresado

def saludar(nombre):

  print(f"¡Hola {nombre}!")

#Ejemplo

saludar("Fabián")

![image](https://github.com/user-attachments/assets/5404b214-0962-44c6-bf09-687b7d7f102a)

![image](https://github.com/user-attachments/assets/714da472-2f80-46f3-96bc-0dba504a87cf)

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

print(factorial(5))

![image](https://github.com/user-attachments/assets/f0b2e6ae-4cc8-4182-b2bc-8014d6927620)

![image](https://github.com/user-attachments/assets/e8a0504a-711d-491b-80c9-4b5769dedf5a)

PUNTO #4

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def calcular_factura(sin_iva, iva=21):
    
  #Calcula el total de una factura incluyendo IVA.
    
  total = sin_iva * (1 + iva / 100)
 return total

# Ejemplo de uso

print(calcular_factura(100))

![image](https://github.com/user-attachments/assets/8444c39b-006e-475f-95de-8a59f91b772d)

![image](https://github.com/user-attachments/assets/e821c4d5-79f3-404e-8093-4e55cb7788d2)

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

print(area_circulo(5))  

print(volumen_cilindro(5, 10)) 

![image](https://github.com/user-attachments/assets/3c0d46d6-3d95-4041-aebc-6fbf8242b2f3)

![image](https://github.com/user-attachments/assets/66d465d7-e164-4575-820f-968ec6256a34)

PUNTO #6

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")

def validar_email(email):

 #Verifica si un email es válido (contiene '@').    
 
 return '@' in email

# Ejemplo de uso

print(validar_email("usuario@ejemplo.com")) 

![image](https://github.com/user-attachments/assets/135eaf1f-2c04-4c72-9a7f-aded2b8da7cc)

![image](https://github.com/user-attachments/assets/be7d8960-9f5b-4bd2-83d0-4dbed24c180e)

PUNTO #7

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

![image](https://github.com/user-attachments/assets/65bd50db-9c11-49e3-b79e-d22c23ab6a4d)

![image](https://github.com/user-attachments/assets/ed0f39ac-41c8-462c-b589-b67c3d841423)

PUNTO #8

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def mayor_de_tres(a, b, c):
    
#Devuelve el mayor de tres números.
    
 return max(a, b, c)

# Ejemplo de uso

print(mayor_de_tres(10, 20, 15)) 

![image](https://github.com/user-attachments/assets/9342c9c7-7017-4554-8b6c-2c1733d22b13)

![image](https://github.com/user-attachments/assets/c889e3a7-7e80-4846-a585-7f44d86e1eb8)

PUNTO #9

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
    
# Ejemplo de uso

print(suma([1, 2, 3, 4]))  

print(multiplicar([1, 2, 3, 4]))  

![image](https://github.com/user-attachments/assets/f25735c2-c8f9-43b0-8ded-19df7b88f32f)

![image](https://github.com/user-attachments/assets/452f25d0-5326-4758-b99e-65f20413cc8f)

PUNTO #10

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def es_vocal(caracter):

#Verifica si un carácter es una vocal.
   
 return caracter.lower() in 'aeiou'

# Ejemplo de uso

print(es_vocal('a'))  

print(es_vocal('b'))  

![image](https://github.com/user-attachments/assets/f28933b2-1f3d-498e-a235-9f1b05f3755e)

![image](https://github.com/user-attachments/assets/48a2b095-39ea-44ed-bffb-70d30f322359)

PUNTO #11

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

![image](https://github.com/user-attachments/assets/7fdee405-3cb9-4d18-b6a9-b3d57c11d688)

![image](https://github.com/user-attachments/assets/d57c45d9-b944-4c3d-9818-d9d46b154827)
