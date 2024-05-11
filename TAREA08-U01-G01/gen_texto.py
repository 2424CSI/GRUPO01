import random
import string

def generar_palabra(longitud):
    return ''.join(random.choices(string.ascii_letters, k=longitud))

def generar_texto(n):
    texto = ' '.join(generar_palabra(random.randint(1, 10)) for _ in range(n))
    return texto

n = int(input("Ingrese la cantidad de palabras que desea generar: "))
texto_generado = generar_texto(n)

with open('texto_generado.txt', 'w') as f:
    f.write(texto_generado)