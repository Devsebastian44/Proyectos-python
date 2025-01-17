from smb.SMBConnection import SMBConnection  # Importar el módulo SMBConnection para interactuar con servidores SMB

# Crear una conexión SMB
conn = SMBConnection('Sebastian', 'python 444', 'nube', 'WORKGROUP', use_ntlm_v2=True)

# Intentar conectar al servidor SMB especificado
if conn.connect('10.10.10.1', 445):  # Dirección IP del servidor y el puerto (445 es el predeterminado para SMB)
    # Si la conexión es exitosa, imprimir un mensaje de éxito
    print("Conexión exitosa")

    # Obtener la lista de archivos y directorios en la carpeta 'Respaldo' en el servidor
    files = conn.listPath('Respaldo', '')  # 'Respaldo' es el nombre del recurso compartido

    # Imprimir los nombres de los archivos y directorios encontrados en la carpeta
    for file in files:
        print(file.filename)

    # Cerrar la conexión SMB después de completar las operaciones
    conn.close()
else:
    # Si la conexión falla, imprimir un mensaje de error
    print("Error al conectar al servidor")
