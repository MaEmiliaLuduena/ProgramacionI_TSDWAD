
numero1 = int(input("Ingrese primer número:"))
numero2 = int(input("Ingrese segundo número:"))
numero3 = int(input("Ingrese tercer número:"))

nMasGrande = numero1

if numero2 > numero1: 
    nMasGrande = numero2
if numero3 > numero1:
    nMasGrande = numero3
print("El número más grande es:", nMasGrande)