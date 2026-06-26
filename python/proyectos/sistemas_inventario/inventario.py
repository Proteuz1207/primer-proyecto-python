# =====================
# DATOS DEL ALMACÉN
# =====================
almacen = [
    {"nombre": "arroz", "precio": 50, "stock": 100},
    {"nombre": "pollo", "precio": 95, "stock": 98},
    {"nombre": "huevo", "precio": 210, "stock": 1003},
    {"nombre": "leche", "precio": 75, "stock": 50},
    {"nombre": "pan", "precio": 95, "stock": 0},
    {"nombre": "aceite", "precio": 75, "stock": 0},
    {"nombre": "lechuga", "precio": 95, "stock": 0}
]

# =====================
# FUNCIONES
# =====================
def ver_stock(producto):
    if producto["stock"] > 0:
        return "disponible"
    else:
        return "no disponible"

def filtrar_por_precio(inventario, precio_maximo):
    return [producto for producto in inventario if producto["precio"] < precio_maximo]

# =====================
# PROCESAMIENTO
# =====================

# Modificar precio del arroz
for producto in almacen:
    if producto["nombre"] == "arroz":
        producto["precio"] = 60

# Filtrar productos fuera de rango
almacen = filtrar_por_precio(almacen, 100)

# =====================
# REPORTE FINAL
# =====================
for producto in almacen:
    resultado = ver_stock(producto)
    print(f"{producto['nombre']} : {resultado}")