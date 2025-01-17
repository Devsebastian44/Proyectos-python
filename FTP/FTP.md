## Descarga

### ¿Qué hace este código?

Este script se conecta a un servidor FTP, descarga un archivo especificado desde el servidor y lo guarda en el sistema local.

### ¿Para qué sirve?

1. **Descargar archivos desde servidores FTP:**
   - Permite recuperar archivos desde un servidor remoto que utiliza el protocolo FTP.

2. **Automatización de tareas:**
   - Ideal para sistemas o procesos que necesitan descargar archivos de forma recurrente.

### Características destacadas

- **Conexión segura con credenciales:**
   - Usa un host, nombre de usuario y contraseña para establecer la conexión al servidor FTP.

- **Forzado de codificación UTF-8:**
   - Garantiza que los nombres de archivos con caracteres especiales se manejen correctamente.

- **Uso del comando `RETR`:**
   - Es el comando estándar de FTP para descargar archivos.

- **Manejo de archivos binarios:**
   - Asegura que los datos descargados (como imágenes o documentos) no sufran alteraciones.

### Ejemplo de uso

El script conecta al servidor `ftp.dlptest.com` utilizando las credenciales proporcionadas. Luego, descarga un archivo llamado `some_file.txt` del servidor y lo guarda localmente en el directorio desde donde se ejecuta el script.

### Resultado esperado:
Si el archivo `some_file.txt` existe en el servidor, se descargará correctamente y aparecerá en tu sistema local.

### Limitaciones

1. **Dependencia de credenciales:**
   - Necesitas credenciales válidas (usuario y contraseña) para conectarte al servidor.

2. **Existencia del archivo:**
   - Si el archivo `some_file.txt` no existe en el servidor, el script generará un error.

3. **Seguridad:**
   - Las credenciales FTP están en texto plano, lo cual puede no ser seguro en un entorno de producción.

4. **Protocolos obsoletos:**
   - El protocolo FTP no es seguro por defecto, ya que no cifra los datos. Para mayor seguridad, se recomienda usar FTPS o SFTP.

### Consideraciones

- Asegúrate de que el archivo a descargar exista en el servidor y que tengas los permisos necesarios para acceder a él.
- Cambia las credenciales y el nombre del archivo según tu entorno.
- Usa SFTP o FTPS en lugar de FTP para mayor seguridad en sistemas reales.


## Directorios

### ¿Qué hace este código?

Este script se conecta a un servidor FTP público, navega por un directorio específico y lista los archivos presentes con detalles como tamaño, permisos, fecha de modificación, etc.

### ¿Para qué sirve?

1. **Explorar servidores FTP:**
   - Accede y lista directorios y archivos en un servidor remoto.

2. **Obtener información detallada:**
   - Extrae datos como tamaño, permisos, y fecha de modificación de archivos.

3. **Automatización:**
   - Facilita la interacción con servidores FTP para tareas repetitivas o análisis.

### Características destacadas

- **Cambio de directorios:**
   - Permite navegar por diferentes rutas del servidor FTP.
   
- **Comandos FTP:**
   - Utiliza `LIST`, `NLST` y `MLSD` para extraer información de archivos y directorios.


## Subida

### ¿Qué hace este código?

Este script permite conectarse a un servidor FTP, cargar un archivo local y listar los archivos y directorios en el servidor.

### ¿Para qué sirve?

1. **Subir archivos a un servidor FTP:**
   - Permite transferir archivos locales a un servidor remoto.

2. **Listar contenido del servidor:**
   - Visualiza los archivos y directorios presentes en el servidor después de cargar un archivo.

3. **Automatización:**
   - Facilita tareas de carga y gestión de archivos en servidores FTP.

### Características destacadas

- **Conexión al servidor:**
   - Establece conexión utilizando credenciales proporcionadas.

- **Carga de archivos:**
   - Usa el comando `STOR` para transferir un archivo local al servidor.

- **Exploración del servidor:**
   - Lista los archivos y directorios presentes en el servidor después de cargar el archivo.

### Ejemplo de uso

Este script conecta al servidor `ftp.dlptest.com`, carga el archivo local `some_file.txt` al directorio actual del servidor y lista el contenido.

### Resultado esperado:

1. El archivo `some_file.txt` será subido al servidor.
2. Se imprimirá en consola una lista de los archivos y directorios presentes en el servidor.

### Limitaciones

1. **Acceso restringido:**
   - Solo funcionará si las credenciales proporcionadas tienen permisos de escritura en el servidor.

2. **Conexión insegura:**
   - Este script usa FTP, que no cifra los datos ni las credenciales. Para mayor seguridad, considera usar FTPS o SFTP.

### Consideraciones

- Asegúrate de que el archivo `some_file.txt` exista en el sistema local.
- Verifica las credenciales y permisos antes de ejecutar el script.
- Para ambientes sensibles, utiliza protocolos seguros como FTPS o SFTP.


