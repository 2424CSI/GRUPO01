import hashlib
import time
import os

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    archivos_a_procesar = ['10pa.txt', '100pa.txt', '1000pa.txt', '10k.txt', '100k.txt', '1mill.txt', '10mill.txt']
    # archivos_a_procesar = ['10pa.txt', '100pa.txt', '1000pa.txt']

    # Procesar cada archivo que termine en .txt
    for filename in files:
        if filename in archivos_a_procesar:
            start_time = time.time()

            with open(os.path.join(dir_path, filename), "r") as file:  # Usar la ruta para abrir el archivo
                text = file.read().strip()

            end_time = time.time()
            read_time = (end_time - start_time) * 1000  # Convertir a milisegundos

            # Etapa 2: Generar e imprimir el hash SHA-256 del texto
            start_time1 = time.time()
            hash = sha256(text)
            end_time1 = time.time()
            read_time1 = (end_time1 - start_time1) * 1000  # Convertir a milisegundos

            print("Archivo:", filename)
            print("Cantidad de caracteres de entrada:", len(text))
            print("Hash SHA-256 del texto:", hash)
            print("Cantidad de caracteres resultantes:", len(hash))

            # Imprimir tiempo de ejecución
            print("Tiempo de lectura del archivo:", read_time, "ms")
            print("Tiempo de cifrado del archivo:", read_time1, "ms")
            print()

            # Guardar los resultados en un archivo
            with open('resultados_sha_256.txt', 'a') as f:
                f.write(f"Archivo: {filename}\n")
                f.write(f"Cantidad de caracteres de entrada: {len(text)}\n")
                f.write(f"Hash SHA-256 del texto: {hash}\n")
                f.write(f"Cantidad de caracteres resultantes: {len(hash)}\n")
                f.write(f"Tiempo de lectura del archivo: {read_time} ms\n")
                f.write(f"Tiempo de cifrado del archivo: {read_time1} ms\n\n")

if __name__ == "__main__":
    main()