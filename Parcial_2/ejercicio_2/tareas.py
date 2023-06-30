class Tarea:
    def __init__(self, id, descripcion, estado):
        self.id = id
        self.descripcion = descripcion
        self.estado = estado

class GestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def buscar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None

    def eliminar_tarea(self, id):
        tarea = self.buscar_tarea(id)
        if tarea:
            self.tareas.remove(tarea)
            print("Tarea eliminada.")
        else:
            print("Tarea no encotnrada")

    def cambiar_estado(self, id, nuevo_estado):
        tarea = self.buscar_tarea(id)
        if tarea:
            tarea.estado = nuevo_estado
            print("Estado de la tarea actualizado.")
        else:
            print("No se encontró la tarea.")

    def mostrar_tareas_ascendente(self):
        tareas_ordenadas = sorted(self.tareas, key=lambda tarea: tarea.id)
        for tarea in tareas_ordenadas:
            print(f"Identificador: {tarea.id}")
            print(f"Descripción: {tarea.descripcion}")
            print(f"Estado: {tarea.estado}")
            print("\n")

sistema = GestionTareas()
ejecutar = True

while ejecutar:
    print("-------- Gestion de tareas --------")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Buscar tarea")
    print("4. Cambiar estado de tarea")
    print("5. Mostrar tareas en orden ascendente")
    print("6. Salir")
    print("\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n")
        id = input("Ingrese el id de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        estado = input("Ingrese el estado de la tarea: ")
        tarea = Tarea(id, descripcion, estado)
        sistema.agregar_tarea(tarea)

    elif opcion == "2":
        print("\n")
        id = input("Ingrese el id de la tarea a eliminar: ")
        sistema.eliminar_tarea(id)

    elif opcion == "3":
        print("\n")
        id = input("Ingrese el identificador de la tarea a buscar: ")
        tarea = sistema.buscar_tarea(id)
        if tarea:
            print(f"Tarea encontrada:")
            print(f"Identificador: {tarea.id}")
            print(f"Descripción: {tarea.descripcion}")
            print(f"Estado: {tarea.estado}")
        else:
            print("No se encontró la tarea.")

    elif opcion == "4":
        print("\n")
        id = input("Ingrese el identificador de la tarea a cambiar el estado: ")
        nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
        sistema.cambiar_estado(id, nuevo_estado)

    elif opcion == "5":
        print("\n")
        sistema.mostrar_tareas_ascendente()

    elif opcion == "6":
        print("Usted salio del programa")
        break
    

    else:
        print("Opción inválida.")