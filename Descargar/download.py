import urllib.request  # Importa la librería `urllib.request` para realizar solicitudes HTTP y manejar recursos web.

url = "http://example.com/file.txt"  # Define la URL del archivo que se va a descargar desde la web.
filename = "file.txt"  # Define el nombre con el cual se guardará el archivo descargado.

urllib.request.urlretrieve(url, filename)  # Descarga el archivo desde la URL y lo guarda con el nombre especificado.

