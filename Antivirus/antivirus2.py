import os  # Importa el módulo `os` para trabajar con rutas y archivos en el sistema operativo.
import shutil  # Importa el módulo `shutil` (aunque en este código no se usa, puede servir para mover/copiar archivos en lugar de solo eliminarlos).

# Definir la ruta a escanear
ruta_escaneo = 'D:\\Programacion\\Python\\Antivirus\\Prueba'  # Especifica la ruta del directorio donde se buscarán archivos maliciosos.

# Definir la lista de extensiones de archivos maliciosos
extensiones_maliciosas = ['.exe', '.dll', '.vbs', '.bat']  # Lista de extensiones asociadas con posibles archivos maliciosos.

# Recorrer todos los archivos en la ruta de escaneo
for foldername, subfolders, filenames in os.walk(ruta_escaneo):  # Itera por carpetas, subcarpetas y archivos en la ruta especificada.
    for filename in filenames:  # Itera sobre cada archivo encontrado en la carpeta actual.
        # Verificar si la extensión del archivo es maliciosa
        if any(ext in filename for ext in extensiones_maliciosas):  # Comprueba si el nombre del archivo contiene alguna extensión maliciosa.
            archivo_malicioso = os.path.join(foldername, filename)  # Obtiene la ruta completa del archivo malicioso.
            print(f"Archivo malicioso encontrado: {archivo_malicioso}")  # Imprime un mensaje indicando que se encontró un archivo malicioso.
            # Eliminar el archivo malicioso
            try:
                os.remove(archivo_malicioso)  # Intenta eliminar el archivo identificado como malicioso.
                print(f"Archivo malicioso eliminado: {archivo_malicioso}")  # Mensaje indicando que el archivo fue eliminado correctamente.
            except:  # Captura cualquier error que ocurra al intentar eliminar el archivo.
                print(f"No se pudo eliminar el archivo: {archivo_malicioso}")  # Mensaje de error si el archivo no se pudo eliminar.
