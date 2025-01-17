### ¿Qué es este código?

Este código es un script en Python que monitorea los cambios en una carpeta específica (archivos y subcarpetas) y registra esa información en un archivo de log. Registra detalles sobre la fecha y hora de las modificaciones realizadas en los archivos y carpetas.

### ¿Para qué sirve?

Este código sirve para llevar un registro de los cambios que ocurren en un directorio determinado. Es útil para realizar auditorías de cambios, hacer copias de seguridad o para el monitoreo de directorios en tiempo real. Cada vez que se modifica un archivo o una carpeta, se agrega un registro con la información relevante en el archivo de log.

### Funcionamiento:

1. **Verificación de archivo de log:** Verifica si el archivo de registro existe. Si no, lo crea.
2. **Obtención de fecha y hora actual:** Registra la fecha y hora en que se ejecuta el monitoreo.
3. **Recorrido de carpeta:** Recorre todos los archivos y subcarpetas de la carpeta especificada.
4. **Registro de cambios:** Para cada archivo o subcarpeta modificada, se registra la ruta completa y la fecha de la última modificación.
5. **Archivo de log:** Los cambios se escriben en un archivo de log especificado por el usuario.

### Ejemplo de uso:

Si quieres monitorear los cambios en una carpeta como `D:\Programacion\Python` y registrar esos cambios en un archivo llamado `cambios.log`, solo debes ejecutar el script y proporcionarle estas rutas.

```bash
folder_path = 'D:\Programacion\Python'
log_file = 'cambios.log'
