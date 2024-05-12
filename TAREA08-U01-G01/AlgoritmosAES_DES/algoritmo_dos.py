import os
import time
from Crypto.Cipher import DES
from base64 import b64encode, b64decode


clave = os.urandom(8)  
cipher = DES.new(clave, DES.MODE_ECB)


with open('C:/UCE/8voSemestre/Cripto/AlgoritmosSimetrics/10000000palabras.txt', 'r') as file:
    texto = file.read()


while len(texto) % 8 != 0:
    texto += ' '


print("Texto original:", texto)


inicio_cifrado = time.time()
texto_cifrado = cipher.encrypt(texto.encode())
fin_cifrado = time.time()


texto_cifrado_codificado = b64encode(texto_cifrado).decode('utf-8')


cipher_dec = DES.new(clave, DES.MODE_ECB)


inicio_descifrado = time.time()
texto_descifrado = cipher_dec.decrypt(texto_cifrado).decode()
fin_descifrado = time.time()

print("Texto cifrado:", texto_cifrado_codificado)
print("Tiempo de cifrado: {} ms".format((fin_cifrado - inicio_cifrado)*1000))
print("Tiempo de descifrado: {} ms".format((fin_descifrado - inicio_descifrado)*1000))