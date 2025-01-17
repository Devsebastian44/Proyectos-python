import ftplib  # Biblioteca para trabajar con servidores FTP.

# Credenciales del servidor FTP.
FTP_HOST = "ftp.dlptest.com"  # Dirección del servidor FTP.
FTP_USER = "dlpuser@dlptest.com"  # Usuario del servidor FTP.
FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"  # Contraseña del usuario.

# Conectarse al servidor FTP.
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)  # Inicializa la conexión.
ftp.encoding = "utf-8"  # Configura la codificación para manejar caracteres especiales.

# Nombre del archivo que se desea cargar al servidor.
filename = "some_file.txt"  # Nombre del archivo local.

# Abrir el archivo local en modo lectura binaria.
with open(filename, "rb") as file:
    # Cargar el archivo al servidor usando el comando FTP STOR.
    ftp.storbinary(f"STOR {filename}", file)

# Mostrar el contenido del directorio actual del servidor para verificar la carga.
ftp.dir()

# Cerrar la conexión con el servidor FTP.
ftp.quit()