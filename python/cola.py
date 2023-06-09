class Banco:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, nombre):
        self.clientes.append(nombre)
        print(f"{nombre} ha sido agregado a la cola.")

    def atender_cliente(self):
        if len(self.clientes) > 0:
            cliente = self.clientes.pop(0)
            print(f"{cliente} esta siendo atendido")
        else:
            print("no hay clientes en la cola.")

    def mostrar_cola(self):
        print("Cola:\n")
        if len(self.clientes) > 0:
            for cliente in self.clientes:
                print(cliente)
        else:
            print("no hay clientes en la cola.")


def menu():
    print("1. agregar cliente a la cola")
    print("2. atender cliente")
    print("3. mostrar cola de clientes")
    print("4. salir")
    opcion = int(input("ingrese una opcion: "))
    return opcion


banco = Banco()

while True:
    opcion = menu()

    if opcion == 1:
        nombre = input("ingrese el nombre del cliente: ")
        banco.agregar_cliente(nombre)
    elif opcion == 2:
        banco.atender_cliente()
    elif opcion == 3:
        banco.mostrar_cola()
    elif opcion == 4:
        break
    else:
        print("opcion invalida")
