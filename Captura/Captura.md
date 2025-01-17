## ¿Qué hace este código?

Este script toma capturas de pantalla automáticamente en intervalos de tiempo regulares y las guarda en una carpeta específica. El proceso continúa ejecutándose hasta que el sistema se apaga o el proceso con el PID 1 (el proceso del sistema) termina.

## ¿Para qué sirve?

1. **Capturas automáticas:**
   - Permite tomar capturas de pantalla automáticamente sin intervención del usuario en intervalos regulares.

2. **Monitoreo:**
   - Es útil para monitorear visualmente la actividad en el escritorio o para realizar registros periódicos de lo que está sucediendo en el sistema.

3. **Almacenamiento organizado:**
   - Guarda todas las capturas en una carpeta predefinida para mantener los archivos organizados y accesibles.

## Características destacadas

- **Uso de `pyautogui`:**
   - Utiliza la librería `pyautogui` para capturar la pantalla, lo que permite obtener imágenes de todo lo que está sucediendo en el escritorio.

- **Intervalos configurables:**
   - El intervalo entre cada captura es configurable (en este caso, 5 segundos), lo que permite personalizar el ritmo de las capturas.

- **Verificación de existencia de carpeta:**
   - El script comprueba si la carpeta para guardar las capturas ya existe, y si no es así, la crea automáticamente.

## Ejemplo de ejecución

Cada 5 segundos, el script toma una captura de pantalla y la guarda en una carpeta llamada `capturas`. El nombre de cada archivo es único, basado en la hora actual.

## Limitaciones

- **Dependencia de la librería `psutil`:**
   - El script sigue ejecutándose hasta que el proceso del sistema (PID 1) termina, lo cual podría no ser adecuado si se desea detenerlo de otra forma.

- **Uso intensivo de recursos:**
   - Si el intervalo de captura es demasiado corto, el script podría consumir muchos recursos del sistema, afectando el rendimiento.

- **No personalización del nombre del archivo:**
   - El nombre del archivo se basa solo en el tiempo de ejecución, lo que puede no ser muy informativo si se necesitan identificar las capturas de manera más clara.
