import os  # Importa el módulo `os` para interactuar con el sistema operativo (por ejemplo, para navegar en directorios).
import hashlib  # Importa el módulo `hashlib` para generar hashes, como SHA-256.

def scan_file(path):  # Define una función para escanear un archivo dado su ruta.
    with open(path, 'rb') as f:  # Abre el archivo en modo binario de solo lectura.
        content = f.read()  # Lee todo el contenido del archivo.
    hash = hashlib.sha256(content).hexdigest()  # Calcula el hash SHA-256 del contenido y lo convierte a hexadecimal.
    if hash in malicious_hashes:  # Verifica si el hash coincide con alguno en la lista de hashes maliciosos.
        print(f"WARNING: {path} is infected!")  # Muestra una advertencia si el archivo está infectado.
    else:
        print(f"{path} is clean.")  # Muestra que el archivo está limpio si no coincide con ningún hash malicioso.

def scan_dir(path):  # Define una función para escanear todos los archivos en un directorio y sus subdirectorios.
    for root, dirs, files in os.walk(path):  # Usa `os.walk` para recorrer recursivamente el directorio dado.
        for file in files:  # Itera sobre cada archivo encontrado.
            file_path = os.path.join(root, file)  # Obtiene la ruta completa del archivo.
            scan_file(file_path)  # Escanea el archivo llamando a la función `scan_file`.

# Lista de hashes conocidos como maliciosos (se pueden añadir más hashes).
malicious_hashes = ['a5b69f8e2f9cfaa239deca4ad927f8e4f4d38e4dc153d69f2902af438f61bca7', '...']

# Escanea un directorio específico en busca de archivos infectados.
scan_dir('D:\\Programacion\\Python\\Antivirus\\Prueba')  # Ruta del directorio que se desea escanear.