class Nodo:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, titulo, artista):
        nodo_nuevo = Nodo(titulo, artista)
        if self.primero is None:
            self.primero = nodo_nuevo
            self.ultimo = nodo_nuevo
            return
        nodo_nuevo.anterior = self.ultimo
        self.ultimo.siguiente = nodo_nuevo
        self.ultimo = nodo_nuevo

    def mostrar(self):
        nodo_actual = self.primero
        while nodo_actual is not None:
            print("Título:", nodo_actual.titulo)
            print("Artista:", nodo_actual.artista)
            nodo_actual = nodo_actual.siguiente


lista_reproduccion = ListaDoble()
lista_reproduccion.agregar("Cancion 1", "Artista 1")
lista_reproduccion.agregar("Cancion 2", "Artista 2")
lista_reproduccion.agregar("Cancion 3", "Artista 3")
lista_reproduccion.agregar("Cancion 4", "Artista 4")
lista_reproduccion.agregar("Cancion 5", "Artista 5")
lista_reproduccion.agregar("Cancion 6", "Artista 6")

lista_reproduccion.mostrar()
