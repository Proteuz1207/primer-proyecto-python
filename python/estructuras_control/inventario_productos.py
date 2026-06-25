almacen = [
    {"nombre": "arroz", "precio": 50, "stock": 100},
    {"nombre": "pollo", "precio": 95, "stock": 98},
    {"nombre": "huevo", "precio": 210, "stock": 1003}
]

# 1. Agregar productos nuevos
nuevo_producto1 = {"nombre": "leche", "precio": 75, "stock": 50}
nuevo_producto2 = {"nombre": "pan", "precio": 95, "stock": 0}
almacen.append(nuevo_producto1)
almacen.append(nuevo_producto2)

# 2. Modificar precio del arroz
for producto in almacen:
    if producto["nombre"] == "arroz":
        producto["precio"] = 60

# 3. Eliminar productos sin stock ANTES de imprimir
for producto in almacen:
    if producto["stock"] == 0:
        print(f"Se retiró del inventario: {producto['nombre']}")

almacen = [producto for producto in almacen if producto["stock"] > 0]

# 4. Imprimir inventario final
for producto in almacen:
    print(f"{producto['nombre']} está disponible por ${producto['precio']}")