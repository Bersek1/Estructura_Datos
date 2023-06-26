import math

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista_Enlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def dato(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def calcular_media(self):
        if self.esta_vacia():
            return None
        
        actual = self.cabeza
        suma = 0
        contador = 0
        while actual is not None:
            suma += actual.dato
            contador += 1
            actual = actual.siguiente

        return suma / contador

    def calcular_desviacion(self):
        if self.esta_vacia():
            return None

        media = self.calcular_media()
        actual = self.cabeza
        suma_cuadrados = 0
        contador = 0
        while actual is not None:
            suma_cuadrados += (actual.dato - media) ** 2
            contador += 1
            actual = actual.siguiente

        varianza = suma_cuadrados / contador
        desviacion = math.sqrt(varianza)
        return desviacion

    def imprimir_lista(self):
        if self.esta_vacia():
            print("La lista está vacia.")
        else:
            actual = self.cabeza
            while actual is not None:
                print(actual.dato)
                actual = actual.siguiente



lista = Lista_Enlazada()
lista.dato(10)
lista.dato(20)
lista.dato(30)

lista.imprimir_lista()

media = lista.calcular_media()
print("Media:", media)

desviacion = lista.calcular_desviacion()
print("Desviación estándar:", desviacion)

print("¿La lista está vacía?", lista.esta_vacia())
