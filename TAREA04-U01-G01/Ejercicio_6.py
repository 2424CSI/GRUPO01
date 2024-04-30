# Crear la matriz de cifrado
cifrado = [
    ['*', 'A', 'S', 'D', 'F', 'G'],
    ['Q', 'a', 'b', 'c', 'd', 'e'],
    ['W', 'f', 'g', 'h', 'i', 'j'],
    ['E', 'k', 'l', 'm', 'n', 'o'],
    ['R', 'p', 'q', 'r', 's', 't'],
    ['T', 'u', 'v', 'x', 'y', 'z']
]

mensaje = input("Ingrese el mensaje a cifrar: ").lower()
mensaje_cifrado = ""

# Recorrer cada caracter del mensaje
for char in mensaje:
    encontrado = False
    for i, fila in enumerate(cifrado):
        if char in fila:
            mensaje_cifrado += cifrado[i][0] + cifrado[0][fila.index(char)]
            encontrado = True
            break
    if not encontrado:
        mensaje_cifrado += cifrado[0][0]*2

# Imprimir la matriz de cifrado, el mensaje original y el mensaje cifrado
print("Matriz de cifrado:")
for fila in cifrado:
    print(fila)
print("Mensaje original: ", mensaje)
print("Mensaje cifrado: ", mensaje_cifrado)