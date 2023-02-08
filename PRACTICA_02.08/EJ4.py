from urllib import request
def contador_url(url):
    fichero = request.urlopen(url)
    palabras = fichero.read()
    return len(palabras.split())

url = print("Introduce la url que quieras aquí: ")