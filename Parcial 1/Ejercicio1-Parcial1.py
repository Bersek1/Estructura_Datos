import numpy as np

# se genera las matrices A, B y C
A = np.random.randint (0, 11, size=(4, 4))
B = np.random.randint (0, 11, size=(4, 4))
C = np.random.randint (0, 11, size=(4, 4))

# se calcula A3 y su inversa
matriz_a_tres = np.linalg.matrix_power(A,3)
A3_inversa = np.linalg.inv(matriz_a_tres)

B_inversa = np.linalg.inv(B)

# se hace los calculos de la operación
resultado = np.dot(np.dot(matriz_a_tres, B_inversa), C) + A3_inversa

print("la matriz A es:")
print(A)
print("la matriz B es:")
print(B)
print("la matriz C es:")
print(C)

print("la matriz resultante es:")
print (resultado)


print("matriz A")
print(matriz_a_tres)
