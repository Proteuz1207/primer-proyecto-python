almacen = [
    {"nombre": "arroz", "precio": 50, "stock": 100},
    {"nombre": "pollo", "precio": 95, "stock": 0},
    {"nombre": "huevo", "precio": 210, "stock": 1003}
]

for inventario in almacen:
    cantidad = inventario["stock"]
    nombre_producto = inventario["nombre"]
    precio = inventario["precio"]
    if cantidad > 0:
        print(f"{nombre_producto} está disponible por ${precio}")
    else:
        print(f"{nombre_producto} está agotado")