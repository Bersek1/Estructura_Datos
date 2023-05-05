
filas = int(input("Ingrese el numero de filas a usar:"))
columnas = int(input("Ingrese el numero de columnas a usar:"))

matriz = [[0 for j in range(columnas)] for i in range(filas)]


for i in range(filas):
    for j in range(columnas):
        valor = input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: ")
        matriz[i][j] = valor


print("Matriz ingresada:")
for fila in matriz:
    print(fila)

# Alfabeticamente
for fila in matriz:
    fila.sort()


print("Matriz ordenada por filas:")
for fila in matriz:
    print(fila)

# numéricamente 
for i in range(columnas):
    columna = [matriz[j][i] for j in range(filas)]
    columna.sort()
    for j in range(filas):
        matriz[j][i] = columna[j]


print("Matriz ordenada por columnas:")
for fila in matriz:
    print(fila)
