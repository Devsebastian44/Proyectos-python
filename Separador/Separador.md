## Separador
### ¿Qué hace este código?

Este código organiza automáticamente los archivos de un directorio en carpetas basadas en sus extensiones. Dependiendo de la extensión del archivo, los archivos se moverán a carpetas correspondientes como "images", "audio", "video", "programs", entre otras. Esto ayuda a mantener el directorio ordenado y facilita la gestión de archivos.

### ¿Para qué sirve?

1. **Organizar archivos por tipo:**
   - Este script ayuda a clasificar y organizar archivos en carpetas según su extensión. Por ejemplo, los archivos `.jpg`, `.png` y `.gif` se moverán a la carpeta "images", mientras que los archivos `.mp3` y `.wav` irán a "audio".

2. **Automatización:**
   - Permite realizar la organización de archivos automáticamente sin intervención manual, lo que es útil para usuarios que gestionan grandes cantidades de archivos.

3. **Orden en directorios:**
   - Ayuda a mantener el directorio limpio y estructurado, evitando la acumulación de archivos desordenados.

### Características destacadas

1. **Uso de `glob` para buscar archivos:**
   - Se utiliza el módulo `glob` para buscar archivos con una extensión específica en la carpeta proporcionada.

2. **Creación de carpetas dinámicas:**
   - Si no existe una carpeta correspondiente a la extensión de archivo, el script la crea automáticamente.

3. **Moviendo archivos:**
   - Los archivos se mueven a las carpetas correspondientes usando el módulo `shutil`, asegurando que los archivos estén bien organizados.

4. **Soporte para múltiples extensiones:**
   - El código está preparado para organizar una amplia gama de tipos de archivos, desde imágenes hasta archivos comprimidos, ejecutables y documentos.

### Ejemplo de uso

1. **Ejecutar el script:**
   - Al ejecutar el script, se pedirá al usuario que ingrese el directorio donde se encuentran los archivos a organizar.
   
2. **Clasificación automática:**
   - El script clasificará automáticamente los archivos basándose en su extensión y los moverá a las carpetas correspondientes.

3. **Resultado esperado:**
   - Los archivos se moverán a sus respectivas carpetas, por ejemplo:
     - `.jpg`, `.png`, `.gif` se moverán a una carpeta llamada `images`.
     - `.mp3`, `.wav` se moverán a una carpeta llamada `audio`.
     - `.mp4`, `.webm` se moverán a una carpeta llamada `video`.

### Resultado esperado

- **Archivos organizados:**
  - Al final del proceso, todos los archivos estarán organizados en carpetas específicas dentro del directorio original, como "images", "audio", "video", etc.

- **Mensajes en la consola:**
  - Durante la ejecución, se mostrarán mensajes que indican cuántos archivos fueron encontrados para cada tipo y si se crearon nuevas carpetas.

### Consideraciones

1. **Permisos de escritura:**
   - Asegúrate de tener permisos suficientes para escribir en el directorio y crear carpetas.

2. **Extensiones no soportadas:**
   - Si un archivo no tiene una extensión definida en el diccionario `extensions`, no se moverá.

3. **Directorio de entrada:**
   - El directorio de entrada debe contener archivos con las extensiones definidas en el script para que el proceso tenga éxito.

### Mejoras posibles

1. **Interfaz gráfica:**
   - Se podría agregar una interfaz gráfica para facilitar la selección del directorio.

2. **Filtrado de subdirectorios:**
   - Actualmente, el script solo maneja archivos dentro del directorio proporcionado. Se podría agregar soporte para subdirectorios si se desea organizar archivos dentro de toda la estructura de carpetas.

3. **Verificación de archivos duplicados:**
   - Podría añadirse una verificación para evitar mover archivos duplicados a la misma carpeta.


## Separador 2

### ¿Qué hace este código?

Este código organiza los archivos de un directorio en una carpeta de destino llamada "ordenados". Los archivos se mueven en función de su fecha de modificación, desde el más antiguo hasta el más reciente. El proceso se repite cada 10 segundos.

### ¿Para qué sirve?

1. **Ordenar archivos por fecha:**
   - El código mueve los archivos del directorio a una carpeta de destino ordenados, organizándolos según la fecha de modificación.

2. **Automatización de tareas:**
   - Este script automatiza la tarea de ordenar archivos, útil para gestionar grandes cantidades de archivos descargados en un solo directorio.

3. **Mantenimiento de la organización:**
   - Ayuda a mantener un directorio de descargas limpio y ordenado, moviendo archivos a una carpeta organizada sin intervención manual.

### Características destacadas

1. **Ordenación por fecha de modificación:**
   - Utiliza la función `os.path.getmtime()` para obtener la fecha de modificación de cada archivo y ordenar la lista de archivos antes de moverlos.

2. **Movimiento de archivos a una carpeta organizada:**
   - Los archivos se mueven a una carpeta llamada `ordenados` dentro del mismo directorio para mantenerlos organizados.

3. **Ejecución continua:**
   - El script sigue ejecutándose de forma continua, ordenando los archivos y moviéndolos cada 10 segundos.

### Ejemplo de uso

1. **Ejecutar el script:**
   - Al ejecutar el script, los archivos de un directorio especificado (por ejemplo, "D:/Descargas/word") se moverán automáticamente a una carpeta de nombre "ordenados", clasificados por su fecha de modificación.

2. **Resultados esperados:**
   - Los archivos se moverán de forma ordenada a la carpeta `ordenados`, y el proceso se repetirá cada 10 segundos, asegurando que los archivos más recientes estén siempre al día.

### Resultado esperado

- **Archivos organizados por fecha:**
  - Los archivos estarán organizados en la carpeta `ordenados`, desde el más antiguo hasta el más reciente según su fecha de modificación.

- **Proceso continuo:**
  - El script sigue funcionando cada 10 segundos, manteniendo el directorio de trabajo limpio y ordenado sin intervención manual.

### Consideraciones

1. **Permisos de escritura:**
   - Asegúrate de que el script tenga permisos para mover los archivos y crear carpetas en el directorio de destino.

2. **Carpeta `ordenados`:**
   - Si la carpeta `ordenados` no existe, el script fallará. Se puede agregar una verificación para crearla si no está presente.

3. **Archivos bloqueados:**
   - Si algún archivo está siendo utilizado por otro proceso, el script podría fallar al intentar moverlo. 

4. **Tiempo de espera:**
   - El script espera 10 segundos entre cada ciclo, lo que podría ajustarse según las necesidades del usuario.
   
### Mejoras posibles

1. **Verificación de existencia de la carpeta `ordenados`:**
   - Se podría agregar un código que verifique si la carpeta `ordenados` existe y la cree si no está presente.

2. **Notificaciones:**
   - Se pueden agregar notificaciones o registros (logs) para informar al usuario sobre el estado del proceso (por ejemplo, cuántos archivos se han movido).

3. **Interfaz gráfica:**
   - Sería posible crear una interfaz gráfica para seleccionar el directorio y personalizar la configuración de tiempo de espera.