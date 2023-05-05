import 'dart:math';

void main() {
  final random = Random();
  final listLength = random.nextInt(1) + 30; // entre 10 y 30
  final List<int> numeros =
      List.generate(listLength, (h) => random.nextInt(11)); // entre 0 y 10

  numeros.sort();
  numeros.shuffle();
  print(numeros);
}
