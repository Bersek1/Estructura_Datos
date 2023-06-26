class Nodo:
    def __init__(self, fruta):
        self.fruta = fruta
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabecera = None
        self.cola = None
    
    def agregar_al_inicio(self, fruta):
        nodo_nuevo = Nodo(fruta)

        if self.cabecera is None:
            self.cabecera = nodo_nuevo
            self.cola = nodo_nuevo
        else:
            nodo_nuevo.siguiente = self.cabecera
            self.cabecera = nodo_nuevo
    
    def agregar_al_final(self, fruta):
        nodo_nuevo = Nodo(fruta)

        if self.cabecera is None:
            self.cabecera = nodo_nuevo
            self.cola = nodo_nuevo
        else:
            self.cola.siguiente = nodo_nuevo
            self.cola = nodo_nuevo
    
    def imprimir_lista(self):
        lista_actual = self.cabecera

        if lista_actual is None:
            print("la lista esta vacia.")
        else:
            print("las frutas que estan en la lista son:")
            while lista_actual is not None:
                print(lista_actual.fruta)
                lista_actual = lista_actual.siguiente
                
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

        print(f"la fruta '{fruta}' no esta en la lista.")   
            
        
def mostrar_menu():
    print("\n--- Menu ---")
    print("A) Agregar fruta al final de la lista")
    print("B) Agregar fruta al inicio de la lista")
    print("C) Eliminar fruta")
    print("D) Imprimir lista")
    print("E) Obtener cabecera")
    print("F) Obtener cola")
    print("S) Salir")
    
    return input("Ingrese una opción: ")

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
