import random
import array

n = random.randint(10, 30)


arr = array.array('i', [random.randint(0, 99) for _ in range(n)])

print("Arreglo random:", arr)


elem = int(input("ingrese el numero que desea buscar en el arreglo:"))

if elem in arr:
    print(f"El elemento {elem} está en el arreglo.")
else:
    print(f"El elemento {elem} no está en el arreglo.")
