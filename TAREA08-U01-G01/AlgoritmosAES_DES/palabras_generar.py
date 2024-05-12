

from faker import Faker

def generar_texto(n, idioma='en_US'):
    fake = Faker(idioma)
    texto = ' '.join(fake.word() for _ in range(n))
    return texto

n = int(input("Ingrese la cantidad de palabras que desea generar: "))

texto_generado = generar_texto(n)  # Assign the generated text to the variable "texto_generado"

with open('C:/UCE/8voSemestre/Cripto/AlgoritmosSimetrics/10000000palabras.txt', 'w') as f:
    f.write(texto_generado)