import hashlib  # Biblioteca para trabajar con funciones hash (como SHA-256).


print("\033[34m   ___ ___               .__   ___.                   \033[0m")
print("\033[34m  /   |   \_____    _____|  |__\_ |__   _______  ___  \033[0m")
print("\033[34m /    ~    \__  \  /  ___/  |  \| __ \ /  _ \  \/  /  \033[0m")
print("\033[34m \    Y    // __ \_\___ \|   Y  \ \_\ (  <_> >    <   \033[0m")
print("\033[34m  \___|_  /(____  /____  >___|  /___  /\____/__/\_ \  \033[0m")
print("\033[34m        \/      \/     \/     \/    \/            \/  \033[0m")


# Solicitar al usuario la ubicación del archivo que se desea analizar.
filename = input("\033[1m\n[+] Ingresa la ubicación del archivo para analizar: \033[0m")

# Crear un objeto hash utilizando el algoritmo SHA-256.
hasher = hashlib.sha256()

# Abrir el archivo en modo de lectura binaria para procesar su contenido.
with open(filename, "rb") as f:
    # Leer el archivo en bloques de 4096 bytes (4 KB) para manejar archivos grandes.
    block = f.read(4096)
    while len(block) > 0:
        hasher.update(block)  # Actualizar el hash con el contenido del bloque leído.
        block = f.read(4096)  # Leer el siguiente bloque.

# Obtener el valor final del hash como una cadena hexadecimal.
hash_value = hasher.hexdigest()

# Imprimir el hash calculado del archivo.
print("\033[1m\nHash SHA-256 de\033[0m", filename, ":", hash_value)

# Abrir el archivo que contiene una lista de hashes maliciosos conocidos.
with open('D:\\Programacion\\Python\\Sandboxed\\hash.txt', 'r') as f:
    lista_hashes = f.readlines()  # Leer todas las líneas del archivo.

# Limpiar la lista de hashes eliminando caracteres extra como espacios o saltos de línea.
lista_hashes = [hash.strip() for hash in lista_hashes]

# Comparar el hash calculado con la lista de hashes maliciosos.
for i, hash in enumerate(lista_hashes):
    if hash == hash_value:  # Verificar si el hash coincide con alguno malicioso.
        print(f"\033[1mEl hash es malicioso\033[0m")  # Indicar que es malicioso.
        break
else:
    print("\033[1mEl hash no es malicioso\033[0m")  # Indicar que no es malicioso.