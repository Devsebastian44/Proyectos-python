## ¿Qué hace este código?

Este script solicita una entrada del usuario y actúa en función de la opción ingresada. Si el usuario no ingresa nada, se le pide una entrada válida. Si ingresa la opción "1", se imprime "XD". Si se ingresa cualquier otra opción válida, el programa termina.

## ¿Para qué sirve?

1. **Interacción con el usuario:**
   - Permite al programa interactuar con el usuario a través de la consola, brindando opciones y respondiendo según la entrada recibida.

2. **Gestión de entradas vacías:**
   - Si el usuario no ingresa nada, el programa solicita una entrada válida, evitando que se continúe con una entrada vacía.

3. **Salida del bucle con entrada válida:**
   - El bucle se detiene cuando el usuario ingresa una opción válida (cualquier valor distinto de "1" y no vacío).

## Características destacadas

- **Uso de `os.system`:**
   - La función `os.system("cls")` limpia la pantalla en sistemas Windows, mientras que `os.system("clear")` lo hace en sistemas Unix (Linux/macOS).

- **Bucle `while True`:**
   - El bucle infinito garantiza que el programa siga pidiendo al usuario una entrada hasta que se ingrese una opción válida o se decida salir con un valor distinto.

- **Manejo de entradas no válidas:**
   - El script maneja entradas vacías mostrando un mensaje para que el usuario ingrese una entrada válida.

## Limitaciones

- **Dependencia de la terminal:**
   - El uso de `os.system("cls")` y `os.system("clear")` depende del sistema operativo y no funcionará en algunos entornos que no sean de consola o terminal.
   
- **Bucle infinito:**
   - El bucle solo se rompe si el usuario ingresa una opción válida distinta de "1". Si se desea agregar más opciones, se debe modificar el código.

