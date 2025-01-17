import os
import time

def log_changes(folder_path, log_file):
    # Verificar si el archivo de registro existe
    if not os.path.exists(log_file):
        # Crear el archivo de registro si no existe
        open(log_file, 'w').close()

    # Obtener la fecha y hora actual
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Abrir el archivo de registro en modo de escritura (append)
    with open(log_file, 'a') as f:
        f.write(f'--- Cambios en la carpeta {folder_path} ({current_time}) ---\n')

        # Recorrer los archivos y subcarpetas de la carpeta
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Obtener la fecha y hora de la última modificación del archivo
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))
                f.write(f'Archivo modificado: {file_path} ({modified_time})\n')

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                # Obtener la fecha y hora de la última modificación de la carpeta
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(dir_path)))
                f.write(f'Carpeta modificada: {dir_path} ({modified_time})\n')

        f.write('\n')

# Ejemplo de uso
folder_path = 'D:\Programacion\Python'  # Reemplazar con la ruta de la carpeta que deseas monitorear
log_file = 'cambios.log'  # Nombre del archivo de registro

log_changes(folder_path, log_file)