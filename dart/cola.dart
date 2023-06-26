class Cola {
  List<String> _clientes = [];

  bool estaVacia() {
    return _clientes.isEmpty;
  }

  void encolar(String cliente) {
    _clientes.add(cliente);
  }

  String? desencolar() {
    if (estaVacia()) {
      return null;
    }
    return _clientes.removeAt(0);
  }
}

void atenderClientes(Cola cola) {
  while (!cola.estaVacia()) {
    String? cliente = cola.desencolar();
    print('Atendiendo al cliente: $cliente');
  }
}

void main() {
  Cola colaClientes = Cola();
  colaClientes.encolar('Cliente 1');
  colaClientes.encolar('Cliente 2');
  colaClientes.encolar('Cliente 3');

  atenderClientes(colaClientes);
}
