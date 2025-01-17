import os.path  # Importar el módulo os.path para interactuar con rutas y verificar la existencia de archivos.
import time  # Importar el módulo time para trabajar con fechas y horas.

def log_edit(file_path):
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe.")  # Si el archivo no existe, imprimir un mensaje y salir de la función.
        return

    # Obtener la fecha y hora actual en formato de cadena (YYYY-MM-DD HH:MM:SS)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Obtener la fecha y hora de la última modificación del archivo en formato de cadena (YYYY-MM-DD HH:MM:SS)
    mod_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(file_path)))

    # Abrir el archivo de registro ("registro.log") en modo "append" para agregar entradas sin sobrescribir el contenido existente
    with open("registro.log", "a") as log_file:
        # Escribir el registro en el archivo de log con la información del archivo editado y las fechas
        log_file.write(f"El archivo {file_path} fue editado el {mod_time} ({current_time})\n")

# Ejemplo de uso:
# Llamar a la función con dos rutas de archivo diferentes
log_edit("D:\Programacion\Python\Sandboxed\sandbox.py")
log_edit("D:\Programacion\Python\Sandboxed\setup.sh")