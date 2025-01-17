import ftplib  # Para conectarse y trabajar con servidores FTP.
import os  # Para manejar operaciones del sistema operativo.
from datetime import datetime  # Para trabajar con fechas y horas.

# Configuración del servidor FTP.
FTP_HOST = "ftp.ed.ac.uk"  # Dirección del servidor FTP.
FTP_USER = "anonymous"  # Usuario para la conexión (anónimo para servidores públicos).
FTP_PASS = ""  # Contraseña para el usuario (vacía en este caso).

# Función para convertir el tamaño de archivos a un formato legible.
def get_size_format(n, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if n < 1024:
            return f"{n:.2f}{unit}{suffix}"  # Retorna el tamaño en KB, MB, etc.
        n /= 1024

# Función para formatear la fecha y hora a un formato legible.
def get_datetime_format(date_time):
    date_time = datetime.strptime(date_time, "%Y%m%d%H%M%S")  # Convierte la fecha a objeto `datetime`.
    return date_time.strftime("%Y/%m/%d %H:%M:%S")  # Retorna la fecha formateada.

# Inicializar sesión FTP.
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)  # Se conecta al servidor FTP.
ftp.encoding = "utf-8"  # Establece codificación UTF-8 para manejar nombres correctamente.
print(ftp.getwelcome())  # Imprime el mensaje de bienvenida del servidor.

# Cambiar al directorio deseado en el servidor.
ftp.cwd("pub/maps")  # Cambia al directorio "pub/maps".

# Listar el contenido del directorio usando el comando LIST.
print("*"*50, "LIST", "*"*50)
ftp.dir()  # Imprime la lista detallada del contenido del directorio.

# Listar nombres de archivos con el comando NLST.
print("*"*50, "NLST", "*"*50)
print("{:20} {}".format("File Name", "File Size"))
for file_name in ftp.nlst():  # Obtiene una lista de archivos en el directorio.
    file_size = "N/A"
    try:
        ftp.cwd(file_name)  # Comprueba si es un directorio (intentando entrar en él).
    except Exception as e:  # Si no es un directorio:
        ftp.voidcmd("TYPE I")  # Cambia el tipo de transferencia a binario.
        file_size = get_size_format(ftp.size(file_name))  # Obtiene el tamaño del archivo.
    print(f"{file_name:20} {file_size}")

# Utilizar el comando MLSD para obtener información detallada.
print("*"*50, "MLSD", "*"*50)
print("{:30} {:19} {:6} {:5} {:4} {:4} {:4} {}".format("File Name", "Last Modified", "Size",
                                                    "Perm","Type", "GRP", "MODE", "OWNER"))
for file_data in ftp.mlsd():  # Itera sobre la lista detallada.
    file_name, meta = file_data  # Divide los datos en nombre y metadatos.
    file_type = meta.get("type")  # Tipo de archivo (archivo, directorio, etc.).
    if file_type == "file":  # Si es un archivo:
        ftp.voidcmd("TYPE I")  # Cambia a transferencia binaria.
        file_size = get_size_format(ftp.size(file_name))  # Obtiene el tamaño del archivo.
    else:
        file_size = "N/A"  # No aplica tamaño si
