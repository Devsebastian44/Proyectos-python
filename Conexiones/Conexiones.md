## ¿Qué hace este código?

Este script obtiene todas las conexiones de red activas (establecidas) en el sistema, mostrando información detallada sobre la dirección local, la dirección remota, el nombre del proceso y el ID del proceso asociado a cada conexión.

## ¿Para qué sirve?

1. **Monitoreo de conexiones de red activas:**
   - Permite obtener una lista de todas las conexiones remotas activas en el sistema, proporcionando detalles como las direcciones locales y remotas y los procesos asociados.

2. **Seguimiento de procesos y puertos:**
   - Ideal para supervisar las conexiones de red y los procesos que están utilizando puertos específicos, lo que puede ser útil para la administración de la seguridad o la solución de problemas de red.

## Características destacadas

- **Uso de `psutil`:**
   - La librería `psutil` permite acceder a información detallada sobre los procesos y conexiones del sistema, facilitando la obtención de datos sobre las conexiones de red.

- **Filtrado de conexiones establecidas:**
   - El script filtra solo las conexiones que están actualmente establecidas, lo que permite centrarse en las conexiones activas.

- **Detalles completos de las conexiones:**
   - Muestra la dirección local, la dirección remota, el nombre del proceso y el ID del proceso para cada conexión, lo que ofrece una vista completa de la actividad de la red.
## Limitaciones

- **No distingue entre conexiones legítimas o maliciosas:**
   - El script solo muestra las conexiones activas, pero no realiza ninguna evaluación de seguridad sobre si son maliciosas.

- **Dependencia de privilegios:**
   - En algunos sistemas, puede ser necesario ejecutar el script con privilegios de administrador para obtener información completa sobre las conexiones y los procesos.