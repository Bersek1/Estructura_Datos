class Pila {
  List<String> _libros = [];

  bool estaVacia() {
    return _libros.isEmpty;
  }

  void apilar(String libro) {
    _libros.add(libro);
  }

  String? desapilar() {
    if (estaVacia()) {
      return null;
    }
    return _libros.removeLast();
  }
}

void apilarLibros(Pila pila, List<String> libros) {
  for (String libro in libros) {
    pila.apilar(libro);
  }
}

void desapilarLibros(Pila pila) {
  while (!pila.estaVacia()) {
    String? libro = pila.desapilar();
    print('Desapilando libro: $libro');
  }
}

void main() {
  Pila pilaLibros = Pila();
  List<String> libros = ['Libro 1', 'Libro 2', 'Libro 3'];

  apilarLibros(pilaLibros, libros);

  desapilarLibros(pilaLibros);
}
