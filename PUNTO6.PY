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
