hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

min = min + dura
hora = hora + min // 60
min = min % 60
hora = hora % 24
print("El evento duró hasta las ", hora, ":", min, "hs.")