from winotify import Notification, audio, Notifier  # Biblioteca para generar notificaciones en Windows.
import win32console  # Biblioteca para interactuar con la consola en Windows.
import win32gui  # Biblioteca para interactuar con la GUI en Windows.

# Obtener la ventana de la consola.
ventana = win32console.GetConsoleWindow()

# Ocultar la ventana de la consola (parámetro `0`).
win32gui.ShowWindow(ventana, 0)

# Crear una notificación utilizando la biblioteca winotify.
toast = Notification(
    app_id="Cursos",  # Identificador de la aplicación.
    title="Hacking y Ciberseguridad",  # Título de la notificación.
    msg="3.11 Primer fallo - SQLmap 1",  # Mensaje que aparece en la notificación.
    duration="short",  # Duración de la notificación (corta o larga).
    icon=r"D:\Programacion\python\Notificacion\icon.png"  # Ruta del icono que aparecerá en la notificación.
)

# Configurar el sonido para la notificación (por defecto, no en bucle).
toast.set_audio(audio.Default, loop=False)

# Agregar una acción a la notificación, que abrirá una carpeta específica.
toast.add_actions(
    label="Ir",  # Texto del botón.
    launch="D:\Cursos\Hacking y Ciberseguridad\ 2.Ciberseguridad enfocada en Pentesting\Sección 3_ Escaneo y enumeración de vulnerabilidades"  # Ruta o acción al presionar el botón.
)

# Mostrar la notificación.
toast.show()
