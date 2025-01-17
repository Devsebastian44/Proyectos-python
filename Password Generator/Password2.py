import string  # Importar el módulo string para acceder a conjuntos de caracteres predefinidos.
import random  # Importar el módulo random para generar elementos aleatorios.

# Definición de colores para la consola utilizando códigos ANSI (opcional, no se usa en este caso).
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
HEADER = '\033[95m'
IMPORTANT = '\33[35m'
NOTICE = '\033[33m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
UNDERLINE = '\033[4m'
LOGGING = '\33[34m'

# Definir los caracteres que se usarán para generar la contraseña: letras, números y símbolos.
characters = string.ascii_letters + string.digits + string.punctuation

# Generar una contraseña aleatoria de 16 caracteres.
password = ''.join(random.choice(characters) for i in range(16))

# Guardar la contraseña generada en un archivo llamado "clave.key".
with open('clave.key', 'w') as file:
    file.write(password)

# Mostrar la contraseña generada y un mensaje indicando que se ha guardado en un archivo.
print(f"La contraseña generada es: {password}")
print("Se ha guardado la contraseña en el archivo clave.key")