import os  # Importa la librería `os` para interactuar con el sistema operativo.

os.system("cls")  # Limpia la pantalla en sistemas Windows (función de la terminal).
os.system("clear")  # Limpia la pantalla en sistemas Unix (Linux/macOS).

while True:  # Inicia un bucle infinito para seguir solicitando la entrada del usuario.
    user_input = input("Ingrese una opción: ")  # Solicita la entrada del usuario.
    if user_input == "":  # Verifica si el usuario no ingresó nada.
        print("Por favor ingrese una entrada válida")  # Muestra un mensaje pidiendo una entrada válida.
    elif user_input == "1":  # Verifica si la entrada del usuario es "1".
        print("XD")  # Imprime "XD" si la entrada es "1".
    else:  # Si la entrada no es "1" ni vacía, se puede agregar más código aquí.
        break  # Sale del bucle si el usuario ingresó una opción diferente de "1".
