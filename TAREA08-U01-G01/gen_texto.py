import random
import string

def generar_texto(n):
    texto = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    return texto

n = int(input("Ingrese la cantidad de caracteres que desea generar: "))
texto_generado = generar_texto(n)

# Guardar el texto generado en un archivo
with open('texto_generado.txt', 'w') as f:
    f.write(texto_generado)
