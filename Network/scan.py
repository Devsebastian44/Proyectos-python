import psutil  # Biblioteca para obtener estadísticas del sistema como CPU, memoria y redes.
import time  # Biblioteca para manejar tiempos y retardos en la ejecución.
import os  # Biblioteca para interactuar con el sistema operativo.
import pandas as pd  # Biblioteca para manejar y manipular datos estructurados en tablas.

UPDATE_DELAY = 1  # Intervalo de actualización en segundos para la monitorización.

def get_size(bytes):
    """
    Convierte una cantidad de bytes a un formato más legible (KB, MB, GB, etc.).
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:  # Unidades de medida
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"  # Retorna el valor formateado con su unidad.
        bytes /= 1024

# Obtiene estadísticas de entrada/salida de red por interfaz con `pernic=True`.
io = psutil.net_io_counters(pernic=True)

while True:
    # Pausa el programa durante el tiempo definido en `UPDATE_DELAY`.
    time.sleep(UPDATE_DELAY)
    
    # Obtiene las estadísticas de red nuevamente para calcular los cambios.
    io_2 = psutil.net_io_counters(pernic=True)
    
    # Lista para almacenar las estadísticas recopiladas de cada interfaz.
    data = []
    for iface, iface_io in io.items():
        # Calcula la velocidad de subida y descarga comparando estadísticas nuevas y anteriores.
        upload_speed = io_2[iface].bytes_sent - iface_io.bytes_sent
        download_speed = io_2[iface].bytes_recv - iface_io.bytes_recv
        
        # Almacena los datos de la interfaz en un diccionario.
        data.append({
            "iface": iface,  # Nombre de la interfaz de red.
            "Download": get_size(io_2[iface].bytes_recv),  # Total de datos descargados.
            "Upload": get_size(io_2[iface].bytes_sent),  # Total de datos subidos.
            "Upload Speed": f"{get_size(upload_speed / UPDATE_DELAY)}/s",  # Velocidad de subida.
            "Download Speed": f"{get_size(download_speed / UPDATE_DELAY)}/s",  # Velocidad de descarga.
        })
    
    # Actualiza las estadísticas para el próximo ciclo.
    io = io_2
    
    # Crea un DataFrame de Pandas para mostrar los datos en formato tabular.
    df = pd.DataFrame(data)
    
    # Ordena las estadísticas por la cantidad de datos descargados.
    df.sort_values("Download", inplace=True, ascending=False)
    
    # Limpia la pantalla según el sistema operativo para actualizar la vista.
    os.system("cls") if "nt" in os.name else os.system("clear")
    
    # Imprime las estadísticas en un formato tabular legible.
    print(df.to_string())