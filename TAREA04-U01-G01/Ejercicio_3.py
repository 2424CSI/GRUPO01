def cifrado_permutacion_columnas():
    # Solicitar al usuario el número de columnas n
    while True:
        try:
            n = int(input("Ingrese el número de columnas (n): "))
            if n <= 0:
                print("El número de columnas debe ser mayor que 0. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Necesito que me proporciones el valor de n: número de columnas para poder continuar.")
            continue
    
    # Solicitar al usuario el mensaje a cifrar
    mensaje = input("Ingrese el mensaje a cifrar: ")
    
    # Verificar si el mensaje está vacío
    if not mensaje.strip():
        print("Para cifrar necesito que me proporciones un mensaje.")
        return
    
    # Eliminar espacios del mensaje
    mensaje_sin_espacios = mensaje.replace(" ", "")
    
    # Validar que el mensaje tenga la longitud correcta
    if len(mensaje_sin_espacios) > n * n:
        print("El mensaje es demasiado largo para la matriz de cifrado.")
        return
    
    # Crear la matriz de cifrado
    matriz_cifrado = [['*' for _ in range(n)] for _ in range(n)]
    
    # Llenar la matriz con los caracteres del mensaje de manera horizontal
    for i in range(n):
        for j in range(n):
            if i * n + j < len(mensaje_sin_espacios):
                matriz_cifrado[i][j] = mensaje_sin_espacios[i * n + j]
    
    # Imprimir la matriz de cifrado
    print("Matriz de cifrado:")
    for fila in matriz_cifrado:
        print(' '.join(fila))
    
    # Cifrado: Leer la matriz de izquierda a derecha, de arriba a abajo
    mensaje_cifrado = ''.join([matriz_cifrado[j][i] for i in range(n) for j in range(n)])
    
    # Imprimir el mensaje original y el mensaje cifrado
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")

# Ejecutar el programa
cifrado_permutacion_columnas()
