import 'dart:io';

void main() {
  print('Ingrese una lista de numeros enteros:');
  String input = stdin.readLineSync()!;

  // se ingeresa los numeros en un string
  List<String> strNumbers = input.split(',');

  // se convierte el string a una lista
  List<int> numbers = [];
  for (String strNumber in strNumbers) {
    int number = int.parse(strNumber);
    numbers.add(number);
  }

  int sum = 0;
  for (int number in numbers) {
    sum += number;
  }
  print('El string ingresado al principio es: $strNumbers');
  print('La suma de los numeros ingresados es: $sum');
}
