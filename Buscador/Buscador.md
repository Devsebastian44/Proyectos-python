## ¿Qué hace este código?

Este script busca archivos con una extensión específica dentro de un directorio y todos sus subdirectorios. Además, utiliza códigos de color ANSI para resaltar texto en la terminal, aunque en este caso, los colores no se aplican al resultado de la búsqueda.

## ¿Para qué sirve?

1. **Búsqueda específica de archivos:**
   - Permite encontrar archivos que coincidan con una extensión dada, como `.txt`, `.pdf`, `.jpg`, etc.

2. **Automatización de tareas:**
   - Recorre automáticamente todos los subdirectorios del directorio principal, ahorrando tiempo y esfuerzo.

3. **Resultados personalizables:**
   - El usuario define el directorio y la extensión, haciendo el script adaptable a diferentes escenarios.

## Características destacadas

- **Función `buscar_archivos`:**
   - Recorre el sistema de archivos y devuelve una lista con las rutas completas de los archivos que coinciden con la extensión proporcionada.

- **Interactividad:**
   - Solicita al usuario ingresar el directorio y la extensión que desea buscar, haciendo que el programa sea fácil de usar.

- **Preparación para colores:**
   - Define constantes de colores ANSI para resaltar texto en la terminal, lo que podría ser útil si se desea formatear los resultados o mensajes futuros.

## Ejemplo de uso

1. Ingresa la ruta del directorio a buscar:
2. Ingresa la extensión del archivo que quieres encontrar:

El programa mostrará las rutas completas de todos los archivos con la extensión indicada.

## Limitaciones

- **Falta de uso de colores:**
- Aunque los colores están definidos, no se aplican al resultado actual del script.
- **No maneja excepciones:**
- Si el directorio ingresado no existe o no tiene permisos, el programa puede fallar.

