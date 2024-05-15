import time
from sympy import randprime, Mod
from random import randint

# Leer el archivo con el texto del mensaje a cifrar
inicio_leer = time.time()
with open('C:/Users/User/Desktop/Criptografia y seguridad/Textos cripto/10mill.txt', 'r') as file:
    message = file.read()
fin_leer = time.time()

# Generar las claves
inicio_clave = time.time()
p = randprime(1, 100)  # Un número primo grande
g = randint(1, p-1)  # Un número aleatorio en el rango [1, p-1]

# Claves privadas
a = randint(1, p-1)  # Clave privada de Alice
b = randint(1, p-1)  # Clave privada de Bob

# Claves públicas
A = Mod(g**a, p)  # Clave pública de Alice
B = Mod(g**b, p)  # Clave pública de Bob

# Clave compartida
s_A = Mod(B**a, p)  # Clave compartida calculada por Alice
s_B = Mod(A**b, p)  # Clave compartida calculada por Bob

assert s_A == s_B  # Las claves compartidas deben ser iguales

fin_clave=time.time()

print(f"Clave de cifrado/descifrado: {s_A}")

# Cifrar el texto
inicio_cifrado = time.time()
encrypted_message = ''.join(chr(ord(c) + s_A) for c in message)
fin_cifrado = time.time()
print(f"Texto cifrado: {encrypted_message}")

# Descifrar el texto
inicio_descifrado = time.time()
decrypted_message = ''.join(chr(ord(c) - s_A) for c in encrypted_message)
fin_descifrado = time.time()
print(f"Texto descifrado: {decrypted_message}")
print("Tiempo transcurrido en leer el texto: {} ms".format((fin_leer - inicio_leer)*1000))
print("Tiempo de generacion de claves: {} ms".format((fin_clave - inicio_clave)*1000))
print("Tiempo de cifrado: {} ms".format((fin_cifrado - inicio_cifrado)*1000))
print("Tiempo de descifrado: {} ms".format((fin_descifrado - inicio_descifrado)*1000))
