import random

filas = int(input("ingrese la cantidad de filas: "))
columnas = int(input("ingrese la cantidad de columnas: "))
multiplicar = int(input("ingrese el valor a multiplicar: "))

matriz = [[random.randint(0, 10) for x in range(columnas)] for y in range(filas)]

for x in range(filas):
    for y in range(columnas):
        matriz[x][y] *= multiplicar

print("la matriz multiplicada:")
for fila in matriz:
    print(fila)


