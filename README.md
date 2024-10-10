# PR2_Zamarripa_Castro_Erick_Fabi-n
Practica de varios puntos de 11 funciones de proposito variado

PUNTO #1

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def mostrar_saludo():

print("Hey amigos!")

#Llamada a la función

mostrar_saludo()


![image](https://github.com/user-attachments/assets/6090fc6e-34c9-464f-9962-b3a03f321a4d)

![image](https://github.com/user-attachments/assets/0b7163f2-0e0b-49b7-bc33-a0f34fce57f5)

PUNTO #2

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Definira el nombre para imprimirlo junto al texto ya ingresado

def saludar(nombre):

  print(f"¡Hola {nombre}!")

#Ejemplo

saludar("Fabián")

![image](https://github.com/user-attachments/assets/4515cda1-19bc-4964-83b6-0c319826c1b1)

![image](https://github.com/user-attachments/assets/f31f41c1-c46e-42f9-b368-48fac40466ca)

PUNTO #3

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def factorial(n):
   
if n == 1 or n == 0:
     return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo (mayor que 0): "))
            if numero <= 0:
                print("Por favor, ingresa un número mayor que 0.")
            else:
                resultado = factorial(numero)
                print(f"El factorial de {numero} es {resultado}.")
                break
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar un número entero.")

if __name__ == "__main__":
    main()


![image](https://github.com/user-attachments/assets/4ae02a01-ba46-4674-905b-ff03f241ec67)

![image](https://github.com/user-attachments/assets/c338b174-d35d-406a-b556-05c67ff02da9)


PUNTO #4

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Pedir al usuario que ingrese la cantidad sin IVA

cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))

#Pedir al usuario que ingrese el porcentaje de IVA

iva = float(input("Ingrese el porcentaje de IVA: "))

#Calcular el total

total = cantidad_sin_iva + (cantidad_sin_iva * (iva / 100))

#Mostrar el total

print(f"El total de la factura después del IVA es: {total:.2f}")

![image](https://github.com/user-attachments/assets/a87b6821-868b-4983-8611-a320786e44ea)

![image](https://github.com/user-attachments/assets/33835a3d-c626-4905-b44b-4592b8ca97f6)

PUNTO #5

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

![image](https://github.com/user-attachments/assets/4b0353ee-4f8f-4c66-b7d5-fbc3807abdba)

![image](https://github.com/user-attachments/assets/8c36ac15-e695-44d3-88db-cc652d8b76e8)


![image](https://github.com/user-attachments/assets/a6b94574-8cd9-4d64-8f9a-d52bd84c5840)


PUNTO #6

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

#Función para verificar la validez del email

def es_email_valido(email):

  return "@" in email

#Solicitar al usuario que ingrese su dirección de email

email = input("Ingrese su dirección de email: ")

#Verificar la validez del email

if es_email_valido(email):

print("La dirección de email es válida.")

else:

 print("La dirección de email no es válida.")

![image](https://github.com/user-attachments/assets/e09ea14b-a18e-45b9-ab5c-0cfbfd7d11e3)

![image](https://github.com/user-attachments/assets/fa45e903-ed58-48ca-b21a-936fad1f9d7e)

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

#Ejemplo de uso

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

#Ejemplo de uso

print ("El mayor es: ")

print(mayor_de_tres(10, 20, 15))  

![image](https://github.com/user-attachments/assets/ab122263-b5bb-452d-b72e-8e1a8e5f2f1d)

![image](https://github.com/user-attachments/assets/99f2d029-9f5a-495a-b39d-ff9da62a0fb0)


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
print("Los resultados son: ")

print(suma([16, 22, 13, 9]))  

print(multiplicar([17, 28, 20, 14])) 

![image](https://github.com/user-attachments/assets/844559df-08fb-401e-8482-248619fda21f)

![image](https://github.com/user-attachments/assets/fa1c71b2-6f2b-45f2-bd88-77ddf573a0a9)

PUNTO #10

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

def es_vocal(caracter):

#Verifica si un carácter es una vocal.
   
 return caracter.lower() in 'aeiou'

#Ejemplo de uso

print(es_vocal('a'))  

print(es_vocal('b'))  

![image](https://github.com/user-attachments/assets/1cfde91b-79ec-4693-b60c-60cb7845f3cc)

![image](https://github.com/user-attachments/assets/2f6487fb-a304-43a5-928e-fd4b7212dfdb)

PUNTO #11

print("")

print ("Zamarripa Castro Erick Fabián_3W_1220")

print("")

import math

#Función para calcular la distancia entre dos puntos

def calcular_distancia(x1, y1, x2, y2):

return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#Solicitar las coordenadas del primer punto

x1 = float(input("Ingrese la coordenada x del primer punto: "))

y1 = float(input("Ingrese la coordenada y del primer punto: "))

#Solicitar las coordenadas del segundo punto

x2 = float(input("Ingrese la coordenada x del segundo punto: "))

y2 = float(input("Ingrese la coordenada y del segundo punto: "))

#Calcular la distancia

distancia = calcular_distancia(x1, y1, x2, y2)

#Mostrar el resultado

print(f"La distancia entre los puntos es: {distancia:.2f}")

![image](https://github.com/user-attachments/assets/a6514b7a-accd-4129-91d6-391e1ef513c4)

![image](https://github.com/user-attachments/assets/20283199-9c32-4641-88ae-0b319f8b386a)

