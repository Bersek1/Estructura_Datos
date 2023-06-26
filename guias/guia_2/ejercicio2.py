class Cliente:
    def __init__(self, numero_ticket, numero_caja):
        self.ticket = numero_ticket
        self.numero_caja = numero_caja
        self.siguiente = None


class Cola_Atencion:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_cliente(self, ticket, numero_caja):
        nuevo_cliente = Cliente(ticket, numero_caja)
        if self.esta_vacia():
            self.primero = nuevo_cliente
            self.ultimo = nuevo_cliente
            nuevo_cliente.siguiente = self.primero
        else:
            nuevo_cliente.siguiente = self.primero
            self.ultimo.siguiente = nuevo_cliente
            self.ultimo = nuevo_cliente

    def atender_cliente(self):
        if self.esta_vacia():
            print("La cola de atención está vacía.")
            return

        cliente_actual = self.primero
        self.primero = cliente_actual.siguiente
        self.ultimo.siguiente = self.primero
        print(f"Cliente atendido - Ticket: {cliente_actual.ticket}, Caja: {cliente_actual.numero_caja}")

    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola de atención está vacía.")
            return

        cliente_actual = self.primero
        while True:
            print(f"Ticket: {cliente_actual.ticket}, Caja: {cliente_actual.numero_caja}")
            cliente_actual = cliente_actual.siguiente
            if cliente_actual == self.primero:
                break


cola = Cola_Atencion()
cola.agregar_cliente(1, "Caja 1")
cola.agregar_cliente(2, "Caja 2")
cola.agregar_cliente(3, "Caja 3")

cola.mostrar_cola()

cola.atender_cliente()

cola.mostrar_cola()
