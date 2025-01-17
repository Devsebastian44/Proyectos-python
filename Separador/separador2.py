import os
import shutil
import time

# Directorio que contiene los archivos a ordenar
directorio = 'D:/Descargas/word'

while True:
    # Obtener una lista de archivos en el directorio
    archivos = os.listdir(directorio)
    
    # Ordenar la lista de archivos por fecha de modificación (de más antiguo a más nuevo)
    archivos.sort(key=lambda x: os.path.getmtime(os.path.join(directorio, x)))
    
    # Mover los archivos ordenados a una carpeta llamada "ordenados"
    for archivo in archivos:
        shutil.move(os.path.join(directorio, archivo), os.path.join(directorio, 'ordenados', archivo))
    
    # Dormir el programa durante 10 segundos antes de volver a ordenar los archivos
    time.sleep(10)