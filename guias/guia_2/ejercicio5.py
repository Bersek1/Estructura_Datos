class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []

    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)

    def eliminar_subordinado(self, subordinado):
        self.subordinados.remove(subordinado)

    def mostrar_subordinados(self):
        for subordinado in self.subordinados:
            print(subordinado.nombre)

    def __str__(self):
        return f"{self.nombre}, {self.cargo}"

def jerarquia(empleado, nivel=0):
    print(" " * nivel, end="")
    print(empleado)
    for subordinado in empleado.subordinados:
        jerarquia(subordinado, nivel + 1)

if __name__ == "__main__":
    ceo = Empleado("Juan", "CEO")
    d_financiero = Empleado("Pedro", "Director Financiero")
    d_marketing = Empleado("Luis", "Director Marketing")

    ceo.agregar_subordinado(d_financiero)
    ceo.agregar_subordinado(d_marketing)

    gerente_proyecto = Empleado("Ana", "Gerente de Proyecto")
    desarrollador_1 = Empleado("Carlos", "Desarrollador 1")
    desarrollador_2 = Empleado("Miguel", "Desarrollador 2")

    d_financiero.agregar_subordinado(gerente_proyecto)
    gerente_proyecto.agregar_subordinado(desarrollador_1)
    gerente_proyecto.agregar_subordinado(desarrollador_2)

    jerarquia(ceo)
