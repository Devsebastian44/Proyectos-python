import os
import glob
import shutil
import time

# Definición de colores para la consola
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

print("")

# Definición de las extensiones de archivos y las carpetas correspondientes
extensions = {
    "jpg": "images",
    "jpeg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "sql": "sql",
    "exe": "programs",
    "msi": "programs",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "docx": "word",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python",
    "py": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
    "iso": "iso",
}

# Bucle para organizar los archivos en carpetas según sus extensiones
while True:
    if __name__ == "__main__":
        # Solicitar al usuario la ruta del directorio donde están los archivos a ordenar
        path = input("Directorio a ordenar: ")
    
    # Nivel de detalle para la salida del proceso (en este caso está desactivado)
    verbose = 0
    for extension, folder_name in extensions.items():
        # Buscar archivos con la extensión especificada en la ruta dada
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        print(f"[*] Found {len(files)} files with {extension} extension")
        
        # Si no existe la carpeta para la extensión y hay archivos, se crea la carpeta
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            print(f"[+] Making {folder_name} folder")
            os.mkdir(os.path.join(path, folder_name))
        
        # Mover los archivos encontrados a la carpeta correspondiente
        for file in files:
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            if verbose:
                print(f"[*] Moving {file} to {dst}")
            shutil.move(file, dst)
    
    # Esperar 5 segundos antes de ejecutar nuevamente el ciclo (en caso de que se estén moviendo muchos archivos)
    time.sleep(5)