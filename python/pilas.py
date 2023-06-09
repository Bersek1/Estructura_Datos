class Pila:
    def __init__(self):
        self.libros = []

    def esta_vacia(self):
        return len(self.libros) == 0

    def apilar(self, libro):
        self.libros.append(libro)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.libros.pop()


def apilar_libros(pila, libros):
    for libro in libros:
        pila.apilar(libro)


def desapilar_libros(pila):
    while not pila.esta_vacia():
        libro = pila.desapilar()
        print(f"Desapilando: {libro}")


pila_libros = Pila()
libros = ['Libro 1', 'Libro 2', 'Libro 3']

apilar_libros(pila_libros, libros)
desapilar_libros(pila_libros)
