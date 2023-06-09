def calcular_promedio_final(nota_lab1, nota_lab2):
    ponderacion_lab1 = 0.3
    ponderacion_lab2 = 0.7
    promedio_final = (nota_lab1 * ponderacion_lab1) + (nota_lab2 * ponderacion_lab2)
    return round(promedio_final, 1)


estudiantes = {}

for i in range(3):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    nota_lab1 = float(input("Ingrese la nota del Laboratorio N°1: "))
    nota_lab2 = float(input("Ingrese la nota del Laboratorio N°2: "))

    promedio_final = calcular_promedio_final(nota_lab1, nota_lab2)

    estudiantes[nombre_estudiante] = {
        "Asignatura": nombre_asignatura,
        "Nota Laboratorio N°1": nota_lab1,
        "Nota Laboratorio N°2": nota_lab2,
        "Promedio Final": promedio_final
    }

print("\nInformación de los estudiantes:")
for estudiante, datos in estudiantes.items():
    print(f"Estudiante: {estudiante}")
    print(f"Asignatura: {datos['Asignatura']}")
    print(f"Nota Laboratorio N°1: {datos['Nota Laboratorio N°1']}")
    print(f"Nota Laboratorio N°2: {datos['Nota Laboratorio N°2']}")
    print(f"Promedio Final: {datos['Promedio Final']}\n")
