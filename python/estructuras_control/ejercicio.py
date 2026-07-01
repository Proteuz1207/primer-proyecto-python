def reporte_empleado(empleado):
    try:
        salario = empleado["salario"]
    except KeyError:
        salario = "salario no registrado"

    try:
        departamento = empleado["departamento"]
    except KeyError:
        departamento = "departamento no registrado"

    return f"{empleado['nombre']} - salario: ${salario}, departamento: {departamento}"

empleados = [
    {"nombre": "Carlos", "salario": 35000, "departamento": "Ventas"},
    {"nombre": "Sofía", "departamento": "Marketing"},
    {"nombre": "Pedro", "salario": 28000},
    {"nombre": "Ana", "salario": 42000, "departamento": "IT"}
]


for buscar in empleados:
    print(reporte_empleado(buscar))

