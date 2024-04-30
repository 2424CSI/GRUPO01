def cifrado_monoalfabetico(cadena, n):
    # Alfabeto original
    alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_cifrado = alfabeto_original[n:] + alfabeto_original[:n]
    # alfabeto original y el cifrado
    print("Alfabeto original:", alfabeto_original)
    print("Alfabeto cifrado:", alfabeto_cifrado)
    # Ciframos la cadena de caracteres
    cadena_cifrada = ''
    for caracter in cadena.lower():
        if caracter in alfabeto_original:
            indice = alfabeto_original.index(caracter)
            cadena_cifrada += alfabeto_cifrado[indice]
        else:
            cadena_cifrada += caracter
    # cadena original y su resultado cifrado
    print("Cadena original:", cadena)
    print("Cadena cifrada:", cadena_cifrada)

# Solicitamos la cadena de caracteres a cifrar
while True:
    cadena = input("Ingrese la cadena de caracteres a cifrar: ")
    if cadena:
        break
    else:
        print("Ingrese un caracter para cifrar")
# Solicitamos el valor de desplazamiento n
while True:
    try:
        n = int(input("Ingrese el valor de desplazamiento n: "))
        break
    except ValueError:
        print("Ingrese un valor de desplazamiento")
# Ejecucion
cifrado_monoalfabetico(cadena, n)
