import pyautogui  # Importa la librería `pyautogui` para tomar capturas de pantalla.
import time  # Importa el módulo `time` para gestionar intervalos de tiempo.
import os  # Importa el módulo `os` para trabajar con el sistema de archivos.
import psutil  # Importa la librería `psutil` para interactuar con los procesos del sistema.

# Crea una carpeta para guardar las capturas
carpeta = 'capturas'  # Define el nombre de la carpeta donde se guardarán las capturas.
if not os.path.exists(carpeta):  # Verifica si la carpeta no existe.
    os.mkdir(carpeta)  # Si no existe, crea la carpeta.

# Define el intervalo de tiempo entre cada captura
intervalo_captura = 5  # segundos, define cuánto tiempo (en segundos) esperar entre cada captura.

# Toma las capturas y guárdalas en la carpeta hasta que la PC se apague
while psutil.Process().pid != 1:  # Este ciclo continuará hasta que el proceso con PID 1 termine (normalmente el proceso del sistema).
    # Define el nombre del archivo de la captura
    nombre_archivo = f'captura{time.time()}.png'  # Asigna un nombre único al archivo utilizando la hora actual.

    # Toma la captura y guárdala en la carpeta
    screenshot = pyautogui.screenshot()  # Toma una captura de pantalla.
    screenshot.save(os.path.join(carpeta, nombre_archivo))  # Guarda la captura en la carpeta con el nombre generado.

    # Espera el intervalo de tiempo antes de tomar la siguiente captura
    time.sleep(intervalo_captura)  # Pausa la ejecución durante el tiempo especificado antes de la siguiente captura.
