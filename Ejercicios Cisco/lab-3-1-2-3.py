numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |    
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numeroEntero = int(input("Introduce el número:"))

while numeroEntero != numeroSecreto:
	print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
	numeroEntero = int (input("Introduce el número nuevamente:"))
print("¡Bien hecho, muggle! Eres libre ahora")