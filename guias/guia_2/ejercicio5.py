class Empleados:
    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, nombre, cargo, jefe_directo=None):
        empleado = {"Nombre": nombre, "Cargo": cargo, "Subordinados": []}
        self.empleados[nombre] = empleado
        if jefe_directo and jefe_directo in self.empleados:
            self.empleados[jefe_directo]["Subordinados"].append(nombre)

    def eliminar_empleado(self, nombre):
        empleado = self.empleados.pop(nombre, None)
        if empleado:
            subordinados = empleado["Subordinados"]
            for subordinado in subordinados:
                self.eliminar_empleado(subordinado)

            for jefe_directo in self.empleados.values():
                if nombre in jefe_directo["Subordinados"]:
                    jefe_directo["Subordinados"].remove(nombre)
                    jefe_directo["Subordinados"].extend(subordinados)

    def mostrar_jerarquia(self):
        if self.empleados:
            self.mostrar_empleado("Director General", None, 0)
        else:
            print("No hay empleados en la jerarquía.")

    def mostrar_empleado(self, nombre, jefe_directo, nivel):
        empleado = self.empleados[nombre]
        indentacion = " " * nivel
        print(f"{indentacion}- Nombre: {empleado['Nombre']}, Cargo: {empleado['Cargo']}")
        for subordinado in empleado["Subordinados"]:
            self.mostrar_empleado(subordinado, nombre, nivel + 1)

    def obtener_jefe_directo(self, nombre):
        for empleado in self.empleados.values():
            if nombre in empleado["Subordinados"]:
                return empleado["Nombre"]
        return None

jerarquia = Empleados()

jerarquia.agregar_empleado("Director General", "CEO")
jerarquia.agregar_empleado("Gerente de Ventas", "Gerente", "Director General")
jerarquia.agregar_empleado("Gerente de Marketing", "Gerente", "Director General")
jerarquia.agregar_empleado("Supervisor de Ventas", "Supervisor", "Gerente de Ventas")
jerarquia.agregar_empleado("Supervisor de Marketing", "Supervisor", "Gerente de Marketing")
jerarquia.agregar_empleado("Vendedor 1", "Vendedor", "Supervisor de Ventas")
jerarquia.agregar_empleado("Vendedor 2", "Vendedor", "Supervisor de Ventas")
jerarquia.agregar_empleado("Asistente de Marketing", "Asistente", "Supervisor de Marketing")

jerarquia.mostrar_jerarquia()

jefe_directo = jerarquia.obtener_jefe_directo("Vendedor 1")
print(f"Jefe directo: {jefe_directo}")
