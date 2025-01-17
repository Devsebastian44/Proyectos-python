import os  # Importa el módulo `os` para manejar archivos y directorios.

# Definición de constantes de colores para la terminal.
GREEN = '\033[32m'      # Color verde para resaltar texto.
YELLOW = '\033[33m'     # Color amarillo para resaltar texto.
BLUE = '\033[34m'       # Color azul para resaltar texto.
MAGENTA = '\033[35m'    # Color magenta para resaltar texto.
CYAN = '\033[36m'       # Color cian para resaltar texto.
WHITE = '\033[37m'      # Color blanco para resaltar texto.
RESET = '\033[39m'      # Reinicia el color al predeterminado.
HEADER = '\033[95m'     # Color para encabezados.
IMPORTANT = '\33[35m'   # Color para destacar información importante.
NOTICE = '\033[33m'     # Color amarillo para notificaciones.
OKBLUE = '\033[94m'     # Azul para mensajes de confirmación.
OKGREEN = '\033[92m'    # Verde para mensajes exitosos.
WARNING = '\033[93m'    # Amarillo para advertencias.
RED = '\033[91m'        # Rojo para mensajes de error o alerta.
END = '\033[0m'         # Finaliza cualquier formato aplicado.
UNDERLINE = '\033[4m'   # Subraya el texto.
LOGGING = '\33[34m'     # Azul para mensajes de registro.

def buscar_archivos(directorio, extension):  # Define una función para buscar archivos con una extensión específica.
    archivos_encontrados = []  # Lista para almacenar las rutas de archivos encontrados.
    for raiz, directorios, archivos in os.walk(directorio):  # Recorre el directorio y sus subdirectorios.
        for archivo in archivos:  # Itera sobre cada archivo en el directorio actual.
            if archivo.endswith(extension):  # Verifica si el archivo tiene la extensión deseada.
                archivos_encontrados.append(os.path.join(raiz, archivo))  # Agrega la ruta completa del archivo a la lista.
    return archivos_encontrados  # Devuelve la lista de archivos encontrados.

# Ejemplo de uso de la función.
directorio_a_buscar = input("Directorio a buscar: ")  # Solicita al usuario la ruta del directorio a buscar.
extension_a_buscar = input("Extensión: ")  # Solicita al usuario la extensión del archivo a buscar.

archivos_encontrados = buscar_archivos(directorio_a_buscar, extension_a_buscar)  # Llama a la función con los valores proporcionados.

for archivo in archivos_encontrados:  # Itera sobre los archivos encontrados.
    print(archivo)  # Imprime la ruta completa de cada archivo encontrado.