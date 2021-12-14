ingreso=float(input("Ingrese el ingreso anual:"))
if ingreso < 85528:
    impuesto = ((18 * ingreso) / 100) - 556.2
else:
    excedente = ingreso - 85528
    impuesto = 14839.2 + ((32 * excedente) / 100)


impuesto = round(impuesto, 0)
if impuesto < 0.0:
    impuesto = 0.0
    
print("El impuesto es: ", impuesto, "pesos")
