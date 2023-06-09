import 'dart:io';

void main() {
  // Ejemplo de uso de diccionarios
  var diccionario = {
    'nombre': 'Juan',
    'edad': 25,
    'ciudad': 'Lima',
  };

  print('Diccionario:');
  print(diccionario);

  // Obtener las claves del diccionario
  var claves = diccionario.keys;
  print('\nClaves:');
  print(claves);

  // Obtener los valores del diccionario
  var valores = diccionario.values;
  print('\nValores:');
  print(valores);

  // Obtener los pares clave-valor del diccionario
  var items = diccionario.entries;
  print('\nPares clave-valor:');
  print(items);

  // Ejemplo de uso de listas
  var lista = ['Manzana', 'Banana', 'Naranja'];

  // Agregar un elemento al final de la lista
  lista.add('Pera');
  print('\nLista después de agregar un elemento:');
  print(lista);

  // Insertar un elemento en la posición 1 de la lista
  lista.insert(1, 'Uva');
  print('\nLista después de insertar un elemento:');
  print(lista);

  // Extender la lista con otra lista
  var otraLista = ['Sandía', 'Melón'];
  lista.addAll(otraLista);
  print('\nLista después de extenderla:');
  print(lista);

  // Eliminar un elemento de la lista
  lista.remove('Banana');
  print('\nLista después de eliminar un elemento:');
  print(lista);

  // Eliminar y obtener el último elemento de la lista
  var ultimoElemento = lista.removeLast();
  print('\nÚltimo elemento eliminado de la lista: $ultimoElemento');

  // Ordenar la lista en orden ascendente
  lista.sort();
  print('\nLista ordenada:');
  print(lista);

  // Ejemplo de uso de conjuntos (sets)
  var conjunto1 = {1, 2, 3, 4, 5};
  var conjunto2 = {4, 5, 6, 7, 8};

  // Agregar un elemento al conjunto
  conjunto1.add(6);
  print('\nConjunto después de agregar un elemento:');
  print(conjunto1);

  // Eliminar un elemento del conjunto
  conjunto1.remove(3);
  print('\nConjunto después de eliminar un elemento:');
  print(conjunto1);

  // Realizar la intersección entre dos conjuntos
  var interseccion = conjunto1.intersection(conjunto2);
  print('\nIntersección de conjuntos:');
  print(interseccion);

  // Realizar la diferencia entre dos conjuntos
  var diferencia = conjunto1.difference(conjunto2);
  print('\nDiferencia de conjuntos:');
  print(diferencia);

  // Copiar un conjunto
  var copiaConjunto = conjunto1.toSet();
  print('\nCopia del conjunto:');
  print(copiaConjunto);
}
