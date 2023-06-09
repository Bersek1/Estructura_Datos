def calcular_promedio(nota_1,nota_2):
    ponderacion_lab1 = 0.3
    ponderacion_lab2 = 0.7
    promedio_final = (nota_1 * ponderacion_lab1) + (nota_2 * ponderacion_lab2)
    
    return round(promedio_final,1)

estudiantes = {}

for i in range (3):
    nombre_estudiante = input("\nIngrese el nombre del estudiante: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    nota_1 = float(input("Ingrese nota del laboratorio 1: "))
    nota_2 = float(input("Ingrese nota del laboratorio 2: "))
    
    promedio_final = calcular_promedio(nota_1,nota_2)
    
    estudiantes[nombre_estudiante] = {
        "asignatura":nombre_asignatura,
        "nota laboratorio 1":nota_1,
        "nota laboratorio 2":nota_2,
        "promedio final":promedio_final        
    }

print("\nInfo de los estudiantes:\n")
for estudiante, info_estudiante in estudiantes.items():
    print(f"Estudiante: {estudiante}")
    print(f"Asignatura: {info_estudiante['asignatura']}")
    print(f"Nota Laboratorio 1: {info_estudiante['nota laboratorio 1']}")
    print(f"Nota Laboratorio 2: {info_estudiante['nota laboratorio 2']}")
    print(f"Promedio Final: {info_estudiante['promedio final']}\n")