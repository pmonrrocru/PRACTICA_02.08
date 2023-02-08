import os.path
def numeros_fichero(n, m):
    fichero = "tabla-" + str(n) + ".txt"
    if os.path.isfile(fichero):
        file = open(fichero, "r")
        print(file.read(m))
    else:
        print("El fichero con la tabla del " + n + " no existe.")
        return
n = input("Introduce un número entero del 1 al 10: ")
m = input("Introduce un segundo número entero del 1 al 10: ")





