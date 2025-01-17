import mysql.connector  # Biblioteca para conectarse y trabajar con bases de datos MySQL.

# Establecer la conexión con la base de datos.
# Esto permite conectarse a un servidor MySQL especificando las credenciales necesarias.
cnx = mysql.connector.connect(
    user='mouredev_read',  # Nombre de usuario para autenticarse en la base de datos.
    password='mouredev_pass',  # Contraseña del usuario.
    host='mysql-5707.dinaserver.com',  # Dirección del servidor donde se encuentra la base de datos.
    database='moure_test'  # Nombre de la base de datos a la que se conectará.
)

# Crear un cursor para ejecutar consultas SQL.
# Un cursor es un objeto que permite interactuar con la base de datos.
cursor = cnx.cursor()

# Definir la consulta SQL que se desea ejecutar.
# En este caso, se seleccionan todos los registros de la tabla "challenges".
consulta = "SELECT * FROM `challenges`"

# Ejecutar la consulta SQL usando el cursor.
cursor.execute(consulta)

# Obtener los resultados de la consulta.
# fetchall() recupera todas las filas resultantes de la ejecución de la consulta.
resultados = cursor.fetchall()

# Recorrer los resultados e imprimir cada fila.
# Cada fila es una tupla que contiene los datos de una fila de la tabla.
for fila in resultados:
    print(fila)

# Cerrar el cursor para liberar los recursos asociados.
cursor.close()

# Cerrar la conexión con la base de datos.
# Esto asegura que la conexión con el servidor MySQL se termine correctamente.
cnx.close()