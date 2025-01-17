import ftplib  # Importa la biblioteca `ftplib` para trabajar con servidores FTP.

# Dirección del servidor FTP.
FTP_HOST = "ftp.dlptest.com"  # Nombre del host del servidor FTP.
FTP_USER = "dlpuser@dlptest.com"  # Nombre de usuario para autenticarse.
FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"  # Contraseña para autenticarse.

# Conectarse al servidor FTP.
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)  # Crea una conexión FTP con las credenciales proporcionadas.
# Forzar la codificación UTF-8.
ftp.encoding = "utf-8"  # Establece la codificación para manejar correctamente los nombres de archivos y directorios.

# Nombre del archivo que desea descargar del servidor FTP.
filename = "some_file.txt"  # Archivo específico a descargar desde el servidor.

# Abrir un archivo local en modo escritura binaria para guardar los datos descargados.
with open(filename, "wb") as file:
    # Usa el comando RETR (Retrieve) de FTP para descargar el archivo y escribe su contenido localmente.
    ftp.retrbinary(f"RETR {filename}", file.write)

# Salir y cerrar la conexión FTP.
ftp.quit()  # Finaliza la conexión de manera segura.