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

