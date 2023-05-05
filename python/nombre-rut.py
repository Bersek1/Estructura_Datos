
nombres = []
ruts = []


for i in range(5):
    nombre = input("Ingrese nombre de la persona {}: ".format(i+1))
    rut = input("Ingrese RUT de la persona {}: ".format(i+1))
    nombres.append(nombre)
    ruts.append(rut)


print("Lista de nombres original: ", nombres)
print("Lista de RUTs original: ", ruts)

#alfabeticamente
nombres.sort()
#numericamente
ruts.sort()


print("Lista de nombres ordenada: ", nombres)
print("Lista de RUTs ordenada: ", ruts)
