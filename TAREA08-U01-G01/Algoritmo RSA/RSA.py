import rsa
import time

# Genera un par de claves RSA y mide el tiempo de generación de clave
start_time = time.time()
public_key, private_key = rsa.newkeys(2048)
key_generation_time = (time.time() - start_time) * 1000

# Lee el archivo de texto y mide el tiempo de lectura
archivo = "C:/Users/Det-Pc/Desktop/BRYAN/OCTAVO2/Criptografía/RES/10mill.txt"
start_time = time.time()
with open(archivo, "r") as f:
    texto = f.read()
file_reading_time = (time.time() - start_time) * 1000

# Divide el texto en partes más pequeñas (por ejemplo, 200 caracteres)
partes = [texto[i:i+200] for i in range(0, len(texto), 200)]

# Cifra cada parte usando la clave pública y mide el tiempo de cifrado
start_time = time.time()
cifrados = [rsa.encrypt(part.encode(), public_key) for part in partes]
encryption_time = (time.time() - start_time) * 1000

# Descifra cada parte usando la clave privada y mide el tiempo de descifrado
start_time = time.time()
descifrados = [rsa.decrypt(cifrado, private_key).decode() for cifrado in cifrados]
decryption_time = (time.time() - start_time) * 1000

# Concatena las partes descifradas para obtener el texto completo
texto_descifrado = "".join(descifrados)

# Guarda los tiempos en un archivo de texto
with open("C:/Users/Det-Pc/Desktop/BRYAN/OCTAVO2/Criptografía/RES/tiempos.txt", "w") as f:
    f.write(f"Tiempo de generación de clave: {key_generation_time} milisegundos\n")
    f.write(f"Tiempo de lectura del archivo: {file_reading_time} milisegundos\n")
    f.write(f"Tiempo de cifrado: {encryption_time} milisegundos\n")
    f.write(f"Tiempo de descifrado: {decryption_time} milisegundos\n")

# Imprime los resultados y los tiempos medidos
print("Texto original:", texto)
print("Texto descifrado:", texto_descifrado)
print("Tiempo de generación de clave:", key_generation_time, "milisegundos")
print("Tiempo de lectura del archivo:", file_reading_time, "milisegundos")
print("Tiempo de cifrado:", encryption_time, "milisegundos")
print("Tiempo de descifrado:", decryption_time, "milisegundos")
