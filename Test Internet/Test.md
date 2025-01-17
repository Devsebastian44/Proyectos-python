## ¿Qué hace este código?

Este script verifica si el equipo tiene conexión a Internet mediante una solicitud HTTP a Google. Si la conexión es exitosa, muestra un mensaje indicando que hay conexión. Si no se puede realizar la solicitud (por ejemplo, por falta de conexión a Internet), muestra un mensaje indicando que no hay conexión.

## ¿Para qué sirve?

1. **Verificar la conexión a Internet:**
   - El código realiza una solicitud a un servidor externo (Google) para verificar si el equipo está conectado a la red.

2. **Detección de problemas de red:**
   - Permite detectar si hay problemas con la conexión a Internet, mostrando un mensaje informativo.

3. **Manejo de errores:**
   - El script maneja posibles errores, como la falta de conexión o tiempos de espera excedidos, sin hacer que el programa se detenga o falle inesperadamente.

## Características destacadas

1. **Manejo de excepciones:**
   - El script utiliza un bloque `try-except` para gestionar posibles errores de conexión o timeout sin que el programa se detenga abruptamente.

2. **Prueba simple de conexión:**
   - La solicitud se realiza a Google con un tiempo de espera de 5 segundos (`timeout=5`). Si no se recibe respuesta en ese tiempo, el código lo maneja como un error.

3. **Interfaz sencilla:**
   - Al ejecutar el script, se imprime un mensaje en la consola indicando si hay conexión a Internet o no.

## Ejemplo de uso

1. **Ejecutar el script:**
   - Al ejecutar el script, se realizará una solicitud a Google.

2. **Resultado:**
   - Si el script puede acceder a Google sin problemas, se mostrará "Con conexión a internet."
   - Si no se puede acceder (por ejemplo, si el equipo no está conectado), se mostrará "Sin conexión a internet."

## Mejoras posibles

1. **Pruebas adicionales:**
   - Podría agregarse una lista de servidores alternativos para verificar la conexión, en caso de que Google no esté accesible por alguna razón.

2. **Respuesta más detallada:**
   - El script podría imprimir más detalles sobre el error (por ejemplo, el tipo de error) para un diagnóstico más preciso.

3. **Comprobación periódica:**
   - Este script puede modificarse para realizar comprobaciones periódicas de la conexión y notificar al usuario cuando la conexión cambie.

4. **Soporte para otros protocolos:**
   - El script podría extenderse para realizar pruebas de conexión a otros servicios como HTTP, FTP, etc.