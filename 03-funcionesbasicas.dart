main() {
  var op1 = operacion(20, 10, suma);
  var op2 = operacion(20, 10, resta);
  var op3 = operacion(20, 10, mul);
  var op4 = operacion(20, 10, div);
  print(op1);
  print(op2);
  print(op3);
  print(op4);
}

int operacion(int a, int b, Function func) {
  return func(a, b);
}

int suma(int a, int b) {
  return a + b;
}

int resta(int a, int b) {
  return a - b;
}

int mul(int a, int b) {
  return a * b;
}

int div(int a, int b) {
  return a ~/ b;
}
