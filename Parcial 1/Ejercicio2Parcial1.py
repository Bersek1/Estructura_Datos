import numpy as np

# se crea la primera matriz del 1 al 10
A = np.random.randint(1, 11, size=(3, 3))

# se crea la segunda matriz dek 11 al 30
B = np.random.randint(11, 31, size=(3, 3))

# se crea la tercera matriz del -1 al -10
C = np.random.randint(-10, 0, size=(3, 3))

# se calcula el lado izquierdo de la propiedad
lado_izquierdo = np.dot(A + B, C)

# se calcula el lado derecho de la propiedad
lado_derecho = np.dot(A, C) + np.dot(B, C)

# se ompara los resultados con equal
equivalentes = np.array_equal(lado_izquierdo, lado_derecho)

print("matriz A:")
print(A)
print("matriz B:")
print(B)
print("matriz C:")
print(C)

print("Lado izquierdo:")
print(lado_izquierdo)
print("Lado derecho:")
print(lado_derecho)

if equivalentes:
    print("se cumple la prioridad.")