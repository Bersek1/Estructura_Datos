import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1 = listaleatoria(10, 10, 20);

  List<int> lista2 = listaleatoria(10, 10, 20);

  List<int> lista3 = listaingresada(5);

  List<int> listaconcatenada = [];
  listaconcatenada.addAll(lista1);
  listaconcatenada.addAll(lista2);
  listaconcatenada.addAll(lista3);

  double promedio = calcularpromedio(listaconcatenada);

  listaconcatenada.sort();

  print("Lista 1: $lista1");
  print("Lista 2: $lista2");
  print("Lista 3: $lista3");
  print("Lista concatenada: $listaconcatenada");
  print("Promedio: $promedio");
}

List<int> listaleatoria(int cantidad, int rangoMin, int rangoMax) {
  Random random = Random();
  List<int> lista = [];

  for (int i = 0; i < cantidad; i++) {
    int numero = random.nextInt(rangoMax - rangoMin + 1) + rangoMin;
    lista.add(numero);
  }

  return lista;
}

double calcularpromedio(List<int> lista) {
  int suma = lista.reduce((a, b) => a + b);
  double promedio = suma / lista.length;
  return promedio;
}

List<int> listaingresada(int cantidad) {
  List<int> lista = [];

  for (int i = 0; i < cantidad; i++) {
    stdout.write("Ingrese el elemento ${i + 1}: ");
    int elemento = int.parse(stdin.readLineSync()!);
    lista.add(elemento);
  }

  return lista;
}
