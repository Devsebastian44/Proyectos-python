## Script 1
### ¿Qué hace este código?

Este programa es un escáner básico de archivos diseñado para detectar si algún archivo en un directorio tiene un hash SHA-256 que coincide con una lista de hashes maliciosos conocidos (`malicious_hashes`). Si se encuentra una coincidencia, marca el archivo como infectado. Si no, indica que está limpio.

### ¿Para qué sirve?

1. **Detección de malware:** El programa verifica la integridad de los archivos buscando patrones (hashes) conocidos asociados con archivos maliciosos.
2. **Seguridad básica:** Ayuda a prevenir la ejecución de archivos maliciosos al identificar y alertar al usuario antes de que los abra o ejecute.
3. **Revisión de directorios:** Puede escanear todos los archivos de un directorio y sus subdirectorios de forma automática.

**Nota:** Este programa solo detecta archivos cuya huella digital (hash) ya está en la lista `malicious_hashes`. No realiza un análisis dinámico del comportamiento de los archivos ni detecta malware desconocido.


## Script 2

### ¿Qué hace este código?

Este script busca archivos específicos en un directorio y sus subdirectorios para determinar si son maliciosos, basándose en una condición predefinida (en este caso, si el nombre del archivo contiene `"archivo3.txt"`). Si un archivo es considerado malicioso, el script lo elimina del sistema y muestra mensajes informativos sobre el proceso.

### ¿Para qué sirve?

1. **Identificación de archivos maliciosos:**
   - Permite buscar archivos sospechosos basados en un criterio definido por el usuario, como nombres o patrones específicos.

2. **Eliminación de archivos no deseados:**
   - Una vez identificado un archivo malicioso, el script puede eliminarlo automáticamente del sistema para prevenir riesgos.

3. **Automatización de revisiones:**
   - Escanea recursivamente todos los directorios y subdirectorios de una ubicación especificada, simplificando la detección y eliminación de archivos problemáticos.

### Características destacadas

- **Función personalizada:** Usa la función `es_malicioso()` para determinar si un archivo cumple con las condiciones de ser malicioso.
- **Automatización:** Utiliza `os.walk` para recorrer directorios y analizar cada archivo encontrado.
- **Gestión de errores:** Incluye un manejo de excepciones para evitar que errores (como permisos insuficientes) interrumpan la ejecución.

**Nota:** Este script está diseñado para detectar archivos maliciosos en función de criterios simples (como el nombre del archivo). No realiza un análisis profundo del contenido del archivo ni detecta malware desconocido.


## Script 3

### ¿Qué hace este código?

Este script recorre un directorio y sus subdirectorios buscando archivos específicos que coincidan con un conjunto de extensiones consideradas maliciosas. Cuando encuentra un archivo que cumple con los criterios, lo elimina y muestra mensajes informativos sobre el proceso.

### ¿Para qué sirve?

1. **Identificación de archivos maliciosos:**
   - Detecta archivos que tienen extensiones comúnmente asociadas con malware (como `.exe`, `.dll`, `.vbs`, o `.bat`).

2. **Eliminación automática:**
   - Una vez identificados los archivos maliciosos, el script los elimina automáticamente del sistema, contribuyendo a la limpieza y seguridad del directorio escaneado.

3. **Escaneo recursivo:**
   - Permite analizar de manera automática no solo el directorio especificado, sino también todos los subdirectorios contenidos en él.

### Características destacadas

- **Definición de extensiones maliciosas:**
   - Utiliza una lista predefinida (`extensiones_maliciosas`) que el usuario puede personalizar para adaptarla a sus necesidades.

- **Automatización mediante `os.walk`:**
   - Recorre todos los archivos y carpetas dentro del directorio especificado, ahorrando tiempo y esfuerzo.

- **Manejo de errores:**
   - Incluye un bloque `try-except` para evitar que errores (como permisos insuficientes o archivos bloqueados) detengan la ejecución del script.

### Limitaciones

Este script identifica archivos como maliciosos únicamente en función de sus extensiones. No realiza un análisis más profundo del contenido de los archivos ni detecta amenazas que no correspondan a las extensiones especificadas.

**Nota:** Este script es útil como una herramienta básica para la limpieza y prevención, pero no reemplaza un software antivirus completo.
