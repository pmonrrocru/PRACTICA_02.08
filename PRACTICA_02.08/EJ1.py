def tablas_mult(entero):
    fichero = "tabla-" + str(entero) + ".txt"
    file = open(fichero, "w")
    for i in range(1, 11):
        file.write(str(entero) + " * " + str(i) + " = " + str(entero * i) + "\n")
    file.close()
    return



