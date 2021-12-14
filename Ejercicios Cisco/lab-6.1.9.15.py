bandera = False
while not bandera: #Mientras sea verdadero hacer:
    try:
        texto = input ("Ingrese el nombre del archivo: ")
        assert texto.endswith(".txt") == True
        archivo = open(texto, "rt", encoding = "utf-8")
        bandera = True
    except AssertionError: #En el caso de que el usuario ingrese mal el nombre del archivo
        print("Debes introducir correctamente el nombre del archivo")
    except FileNotFoundError: #En caso de que se haya producido un error
        print("No pudimos encontrar tu archivo")
        
        
        
abecedario = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0,
            "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0,
            "ñ" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0,
            "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}

textoTrabajo = ''
for i in archivo:
    i = i.lower()
    textoTrabajo += i

print("Encontramos estos valores en tu texto")

for e in abecedario.keys():
    cuenta = textoTrabajo.count(e)
    abecedario[e] = cuenta
    if cuenta > 0:
        print(e , " -> " , cuenta)
    else:
        continue



        
    
    
    


