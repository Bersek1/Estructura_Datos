import random

fila1 = int(input("ingrese la cantidad de filas de la primera matriz: "))
columna1 = int(input("ingrese la cantidad de columnas de la primera matriz: "))
fila2 = int(input("ingrese la cantidad de filas de la segunda matriz: "))
columna2 = int(input("ingrese la cantidad de columnas de la segunda matriz: "))

matriz1 = []
for x in range(fila1):
    fila = []
    for y in range(columna1):
        fila.append(random.randint(0, 5))
    matriz1.append(fila)

matriz2 = []
for x in range(fila2):
    fila = []
    for y in range(columna2):
        fila.append(random.randint(0, 5))
    matriz2.append(fila)

print("la primera matriz es:")
for fila in matriz1:
    print(fila)
print("la segunda matriz es:")
for fila in matriz2:
    print(fila)

# se suma las dos matrices
if fila1 == fila2 and columna1 == columna2:
    suma_matriz = []
    for x in range(fila1):
        fila = []
        for y in range(columna1):
            fila.append(matriz1[x][y] + matriz2[x][y])
        suma_matriz.append(fila)
    print("Matriz suma:")
    for fila in suma_matriz:
        print(fila)


fila3 = int(input("ingrese la cantidad de filas de la tercera matriz: "))
columna3 = int(input("ingrese la cantidad de columnas de la tercera matriz: "))

# se crea la matriz 3
matriz3 = []
for x in range(fila3):
    fila = []
    for y in range(columna3):
        fila.append(random.randint(0, 5))
    matriz3.append(fila)

#imprime la matriz 3
print("la tercera matriz es:")
for fila in matriz3:
    print(fila)

# se resta matriz sumada anteriormente y se resta con la matriz 3
if fila3 == fila2 and columna3 == columna2:
    resta_matriz = []
    for x in range(fila3):
        fila = []
        for y in range(columna3):
            fila.append(matriz3[x][y] - suma_matriz[x][y])
        resta_matriz.append(fila)
    print("la matriz resultante es:")
    for fila in resta_matriz:
        print(fila)
