import os
import time
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


clave = os.urandom(16)  # AES usa claves de 16, 24 o 32 bytes
cipher = AES.new(clave, AES.MODE_EAX)


with open('C:/UCE/8voSemestre/Cripto/AlgoritmosSimetrics/10000000palabras.txt', 'r') as file:
    texto = file.read()


print("Texto original:", texto)


inicio_cifrado = time.time()
texto_cifrado, tag = cipher.encrypt_and_digest(texto.encode())
fin_cifrado = time.time()


texto_cifrado_codificado = b64encode(texto_cifrado).decode('utf-8')


inicio_descifrado = time.time()
cipher_dec = AES.new(clave, AES.MODE_EAX, nonce=cipher.nonce)
texto_descifrado = cipher_dec.decrypt_and_verify(texto_cifrado, tag)
fin_descifrado = time.time()

print("Texto cifrado:", texto_cifrado_codificado)
print("Tiempo de cifrado: {} ms".format((fin_cifrado - inicio_cifrado)*1000))
print("Tiempo de descifrado: {} ms".format((fin_descifrado - inicio_descifrado)*1000))