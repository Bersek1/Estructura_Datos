class Nodo:
    def __init__(self, fruta):
        self.fruta = fruta
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def agregar_al_final(self, fruta):
        nuevo_nodo = Nodo(fruta)

        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def agregar_al_inicio(self, fruta):
        nuevo_nodo = Nodo(fruta)

        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabecera
            self.cabecera = nuevo_nodo

    def eliminar_fruta(self, fruta):
        actual = self.cabecera
        anterior = None

        while actual is not None:
            if actual.fruta == fruta:
                if anterior is None:
                    self.cabecera = actual.siguiente
                    if actual == self.cola:
                        self.cola = None
                else:
                    anterior.siguiente = actual.siguiente
                    if actual == self.cola:
                        self.cola = anterior
                return

            anterior = actual
            actual = actual.siguiente

        print(f"La fruta '{fruta}' no se encontró en la lista.")

    def imprimir_lista(self):
        actual = self.cabecera

        if actual is None:
            print("La lista está vacía.")
        else:
            print("Frutas en la lista:")
            while actual is not None:
                print(actual.fruta)
                actual = actual.siguiente

    def obtener_cabecera(self):
        if self.cabecera is not None:
            print(f"Cabecera: {self.cabecera.fruta}")
        else:
            print("La lista está vacía.")

    def obtener_cola(self):
        if self.cola is not None:
            print(f"Cola: {self.cola.fruta}")
        else:
            print("La lista está vacía.")


# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("\n--- Menú ---")
    print("A) Agregar fruta al final de la lista")
    print("B) Agregar fruta al inicio de la lista")
    print("C) Eliminar fruta")
    print("D) Imprimir lista")
    print("E) Obtener cabecera")
    print("F) Obtener cola")
    print("S) Salir")

    return input("Ingrese una opción: ").strip().upper()


# Crear una lista enlazada
lista_frutas = ListaEnlazada()

while True:
    opcion = mostrar_menu()

    if opcion == "A":
        fruta = input("Ingrese el nombre de la fruta a agregar al final de la lista: ")
        lista_frutas.agregar_al_final(fruta)
        print("Fruta agregada al final de la lista.")

    elif opcion == "B":
        fruta = input("Ingrese el nombre de la fruta a agregar al inicio de la lista: ")
        lista_frutas.agregar_al_inicio(fruta)
        print("Fruta agregada al inicio de la lista.")

    elif opcion == "C":
        fruta = input("Ingrese el nombre de la fruta a eliminar: ")
        lista_frutas.eliminar_fruta(fruta)

    elif opcion == "D":
        lista_frutas.imprimir_lista()

    elif opcion == "E":
        lista_frutas.obtener_cabecera()

    elif opcion == "F":
        lista_frutas.obtener_cola()

    elif opcion == "S":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
