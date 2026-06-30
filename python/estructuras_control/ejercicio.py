def evaluar_desempeño(empleados):
    if empleados["ventas_mes"] >= empleados["meta"]:
        return "meta cumplida"
    else:
        return "meta no alcanzada"



empleados = [
    {"nombre": "Carlos", "ventas_mes": 15000, "meta": 12000},
    {"nombre": "Sofía", "ventas_mes": 9000, "meta": 12000},
    {"nombre": "Pedro", "ventas_mes": 12000, "meta": 12000}
]


for verificar in empleados:
    resultado = evaluar_desempeño(verificar)
    nombre_empleado = verificar["nombre"]
    print(f"{nombre_empleado}: {resultado}")

# Calculo de precio final

def calcular_precio_final(precio, cantidad, impuesto = 0.18):
    resultado = (precio * cantidad) + (precio * cantidad * impuesto)
    return resultado

print(calcular_precio_final(200, 7))
print(calcular_precio_final(200, 7, 0.10))


