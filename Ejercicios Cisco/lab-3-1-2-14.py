bloques = int(input("Ingrese el número de bloques: "))

capa = 1
altura = 0

while bloques >= capa:
    altura += 1
    bloques -= capa
    capa += 1

print("La altura de la pirámide es: ", altura)
