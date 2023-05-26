import 'dart:math';

void main() {
  final random = Random();
  final listLength = random.nextInt(10) + 30; // entre 10 y 30
  final List<int> numeros =
      List.generate(listLength, (_) => random.nextInt(11)); // entre 0 y 10

  numeros.sort();
  numeros.shuffle();
  print(numeros);
}
