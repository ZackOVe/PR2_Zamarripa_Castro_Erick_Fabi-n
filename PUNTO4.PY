print("")
print ("Zamarripa Castro Erick Fabián_3W_1220")
print("")

# Pedir al usuario que ingrese la cantidad sin IVA
cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))

# Pedir al usuario que ingrese el porcentaje de IVA
iva = float(input("Ingrese el porcentaje de IVA: "))

# Calcular el total
total = cantidad_sin_iva + (cantidad_sin_iva * (iva / 100))

# Mostrar el total
print(f"El total de la factura después del IVA es: {total:.2f}")
