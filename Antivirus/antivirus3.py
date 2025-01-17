import os  # Importa el módulo `os` para manejar rutas de archivos y directorios.

def es_malicioso(archivo):  # Define una función para verificar si un archivo es malicioso.
    if "archivo3.txt" in archivo:  # Comprueba si el nombre del archivo contiene "archivo3.txt".
        return True  # Devuelve True si el archivo es malicioso.
    else:
        return False  # Devuelve False si no es malicioso.

# Recorre el directorio y subdirectorios especificados.
for raiz, carpetas, archivos in os.walk("D:/Programacion/Python/Antivirus/Prueba"):  
    for archivo in archivos:  # Itera sobre cada archivo en el directorio actual.
        ruta_completa = os.path.join(raiz, archivo)  # Obtiene la ruta completa del archivo.
        if es_malicioso(archivo):  # Verifica si el archivo es malicioso usando la función `es_malicioso`.
            print(f"El archivo {ruta_completa} es malicioso")  # Imprime un mensaje indicando que el archivo es malicioso.
            try:
                # Elimina el archivo malicioso.
                os.remove(ruta_completa)  # Intenta eliminar el archivo identificado como malicioso.
                print(f"Archivo eliminado: {ruta_completa}")  # Confirma que el archivo fue eliminado correctamente.
            except Exception as e:  # Captura errores que puedan ocurrir durante la eliminación.
                print(f"Error al intentar eliminar el archivo {ruta_completa}: {e}")  # Muestra un mensaje de error si no se puede eliminar.
