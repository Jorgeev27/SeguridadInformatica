import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

longitud = int(input("Introduce el número de caracteres para la contraseña: "))
contraseña_segura = generar_contraseña(longitud)
print("Tu contraseña segura es:", contraseña_segura)
