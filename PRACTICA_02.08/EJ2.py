def comprobar_tablas(input):
    entero = input("Introduce un número entero del 1 al 10: ")
    fichero = ("tabla-" + str(entero) + ".txt")
    try:
        file = open(fichero, "r")
    except FileNotFoundError:
        print("El fichero con la tabla del " + entero + " no existe.")
    else:
        print(file.read())
        file.close()
    return



