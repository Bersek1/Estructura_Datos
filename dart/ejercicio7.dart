import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista = [];

  stdout.write('ingrese el tamaño de la lista: ');
  int tamano = int.parse(stdin.readLineSync()!);

  for (int i = 0; i < tamano; i++) {
    int numeros;
    do {
      stdout.write('ingrese el numero ${i + 1}:');
      numeros = int.tryParse(stdin.readLineSync()!) ?? -1;
    } while (numeros < 0);
    lista.add(numeros);
  }

  lista.sort();

  print('lista ordenada ascendentemente: $lista');

  lista.sort((a, b) => b.compareTo(a));

  print('lista ordenada descendentemente: $lista');

  int maximo = lista.reduce(max);
  int minimo = lista.reduce(min);

  print('valor maximo de la lista es: $maximo');
  print('Valor minimo de la lista es: $minimo');
}
