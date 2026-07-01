


def obtener_precio(producto):
    try:
     if producto["stock"] > 0:
        precio = producto["precio"]
        return precio * 1.12
    except KeyError:
        return "Dato faltante en el producto"


producto1 = {"nombre": "café", "precio": 120, "stock": 10}
producto2 = {"nombre": "té", "stock": 5}  # sin precio

print(f"El precio del {producto1['nombre']} es: {obtener_precio(producto1)}")
print(f"El precio del {producto2['nombre']} es: {obtener_precio(producto2)}")