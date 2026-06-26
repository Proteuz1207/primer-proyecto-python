def verificar_stock(producto):
    if producto["stock"] > 0:
        return "disponible"
    else:
        return "agotado"

almacen = [
    {"nombre": "arroz", "precio": 50, "stock": 100},
    {"nombre": "pollo", "precio": 95, "stock": 98},
    {"nombre": "huevo", "precio": 210, "stock": 1003},
    {"nombre": "leche", "precio": 75, "stock": 50},
    {"nombre": "pan", "precio": 95, "stock": 0}
]

for producto in almacen:
    resultado = verificar_stock(producto)
    print(f"{producto['nombre']}: {resultado}")