def cifrado_vigenere(cadena_entrada, clave):
    texto_cifrado = ""
    clave = list(clave)
    longitud_clave = len(clave)
    longitud_entrada = len(cadena_entrada)

    # Repito clave hasta que tenga la misma longitud que cadena_entrada
    for i in range(longitud_entrada - longitud_clave):
        clave.append(clave[i % longitud_clave])

    for i in range(longitud_entrada):
        if cadena_entrada[i].isalpha():
            desplazamiento = ord(clave[i].upper()) - ord('A')
            codigo_caracter = ord(cadena_entrada[i].upper()) + desplazamiento
            caracter_cifrado = chr((codigo_caracter - ord('A')) % 26 + ord('A'))
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += cadena_entrada[i]

    return texto_cifrado

cadena_entrada = input("Introduce la cadena a cifrar: ")
clave = input("Introduce la clave de cifrado: ")
texto_cifrado = cifrado_vigenere(cadena_entrada, clave)

print("Cadena de entrada: ", cadena_entrada)
print("Clave de cifrado: ", clave)
print("Cadena cifrada: ", texto_cifrado)