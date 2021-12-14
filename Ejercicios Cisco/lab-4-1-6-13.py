# Ejercicio 4_1_6_13 v1.1 Corregido el 3/6/2021
# Integrantes:
# Maria Coronel
# Franco Leiva
# Maria Emilia Ludueña
# Maria Guadalupe Monge Barale
# Fernando Tejeda
# Natalia Zamudio

from random import randrange

def DisplayBoard(board):

    print("+","-------+"*3 ,sep="")
    for fila in board:
        print("|","       |"*3 ,sep="")
        print("|","       |"*3 ,sep="")
        print("|", end="")
        for columna in fila:
            print("   ", columna, "   |", sep="", end="")    
        print()
        print("|","       |"*3 ,sep="")
        print("|","       |"*3 ,sep="")
        print("+","-------+"*3 ,sep="")
    print() #espacio entre tablero e ingrese movimiento       
print () #espacio entre comienza el juego y tablero


def EnterMove(board):
    
    a=int(input("Ingresa un movimiento: "))
    while(a < 1 or a > 9 ):
       a=int(input("Movimiento no valido, ingrese otro: "))
    
    i=0
    j=0
    ocupada=True
    
    while(ocupada == True):        
        for i in range(3):
            for j in range(3):
                if(board[i][j] == a):
                    board[i][j]="O"
                    ocupada = False
                    break
                
        if(ocupada == True):
            print("Lugar ocupado")
            a=int(input("Ingresa un movimiento: "))
            
            while(a < 1 or a > 9 ):
                a=int(input("Movimiento no valido, ingrese otro: "))
            
                    

def MakeListOfFreeFields(board):
    
    libre = []
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] not in ['O','X']:
                libre.append((fila,columna))
    return libre


def VictoryFor(board, sign):


    if(sign== "X"):
        jugador = "Maquina"
    else:
        jugador = "Usuario"
        
    diagonal1=True
    diagonal2=True
    
    for i in range(3):
        if(board[0][i] == sign and board[1][i] == sign and board[2][i] == sign ):
            print("Gano",jugador,"haciendo columna")
            return jugador
        if(board[i][0] == sign and board[i][1] == sign and board[i][2] == sign ):
            print("Gano",jugador,"haciendo fila")
            return jugador
        
        if(board[i][i]!= sign ):
            diagonal1=False
        if(board[2-i][i] != sign):
            diagonal2=False
            
    if (diagonal1 == True or diagonal2 == True):
        print("Gano",jugador,"haciendo diagonal")
        return jugador
    

    else :
        return "Nadie"
    

def DrawMove(board):
    
    libre = MakeListOfFreeFields(board) # Genero una lista con las posiciones libres

    l=len(libre)                        # Tomo la longitud de la lista, es decir cuantas tuplas tiene esa lista

    posicion = randrange(l)             # Se genera un nro aleatorio, tomando en cuenta la longitud "l" como maximo

    fila,columna=libre[posicion]        # Una asignacion de los valores de la tupla elegida 

    board[fila][columna]= "X"           # coloca una x en la posicion que eligio la maquina
    
    print("Este es el movimiento de la maquina :")
    print()



tablero = []
tablero = [[1,2,3],[4,"X",6],[7,8,9]]
ganador="Nadie"

print("Empieza el juego, la maquina va al medio ")
print ()
DisplayBoard(tablero)

while(len(MakeListOfFreeFields(tablero)) != 0):
    
    EnterMove(tablero)
    DisplayBoard(tablero)
    
    ganador=VictoryFor(tablero,"O")
    if(ganador == "Usuario"):
        print("+","-------+"*3 ,sep="")
        print("+     G A N A S T E     +")
        print("+","-------+"*3 ,sep="")
        break
    
    
    DrawMove(tablero)
    DisplayBoard(tablero)
    
    ganador = VictoryFor(tablero,"X")
    if(ganador == "Maquina"):
        print("+","-------+"*3 ,sep="")
        print("+    P E R D I S T E    +")
        print("+","-------+"*3 ,sep="")
        break

    if(len(MakeListOfFreeFields(tablero))== 0 and ganador == "Nadie"):
        print("+","-------+"*3 ,sep="")
        print("+      E M P A T E      +")
        print("+","-------+"*3 ,sep="")


DisplayBoard(tablero)
print("Termino el juego")



