import os  # Importa el módulo os para trabajar con el sistema de archivos.
import time  # Importa el módulo time para manejar fechas y horas.

def log_changes(folder_path, log_file):  # Define una función para registrar los cambios en una carpeta.
    # Verificar si el archivo de registro existe
    if not os.path.exists(log_file):  
        # Crear el archivo de registro si no existe
        open(log_file, 'w').close()

    # Obtener la fecha y hora actual
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Abrir el archivo de registro en modo de escritura (append)
    with open(log_file, 'a') as f:  
        f.write(f'--- Cambios en la carpeta {folder_path} ({current_time}) ---\n')  
        # Escribe una cabecera con la ruta monitoreada y la fecha/hora actual.

        # Recorrer los archivos y subcarpetas de la carpeta
        for root, dirs, files in os.walk(folder_path):  
            for file in files:  
                file_path = os.path.join(root, file)  
                # Construye la ruta completa del archivo.
                
                # Obtener la fecha y hora de la última modificación del archivo
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))
                f.write(f'Archivo modificado: {file_path} ({modified_time})\n')  
                # Registra el archivo modificado y su fecha/hora de modificación.

            for dir in dirs:  
                dir_path = os.path.join(root, dir)  
                # Construye la ruta completa de la carpeta.

                # Obtener la fecha y hora de la última modificación de la carpeta
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(dir_path)))
                f.write(f'Carpeta modificada: {dir_path} ({modified_time})\n')  
                # Registra la carpeta modificada y su fecha/hora de modificación.

        f.write('\n')  
        # Añade una línea en blanco al final del bloque de cambios registrados.

# Ejemplo de uso
folder_path = 'D:\Programacion\Python'  # Ruta de la carpeta a monitorear (debe reemplazarse según necesidad).
log_file = 'cambios.log'  # Nombre del archivo donde se registrarán los cambios.

log_changes(folder_path, log_file)  # Llama a la función para registrar los cambios.
