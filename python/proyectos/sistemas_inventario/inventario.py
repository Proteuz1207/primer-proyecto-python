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


def calcular_precio_final(stock, precio, cantidad, impuestos = 0.12):
    if stock > 0:
        return (precio * cantidad) + (precio * cantidad * impuestos)    
    else:
        return "No hay inventario de este producto"
    
def obtener_precio(producto):
    try:
        precio = producto["precio"]
        return precio * 1.12
    except KeyError:
        return "Este producto no tiene precio"
def reporte_producto(producto):
    try:
        precio = producto["precio"]
    except KeyError:
        precio = "precio no registrado"
    
    try:
        stock = producto["stock"]
    except KeyError:
        stock = "stock no registrado"
    return f"{producto['nombre']} — precio: ${precio}, stock: {stock}"
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

# Precio a pagar segun el producto este disponible

for buscar in almacen:
    stock = buscar["stock"]
    precio = buscar["precio"]
    nombre = buscar["nombre"]
    resultado = calcular_precio_final(stock, precio, 1)
    print (f"{nombre}  precio final: {resultado}")


producto1 = {"nombre": "café", "precio": 120, "stock": 10}
producto2 = {"nombre": "té", "stock": 5}

print(f"El precio del {producto1['nombre']} es: {obtener_precio(producto1)}")
print(f"El precio del {producto2['nombre']} es: {obtener_precio(producto2)}")

productos = [
    {"nombre": "café", "precio": 120, "stock": 10},
    {"nombre": "té", "stock": 5},
    {"nombre": "azúcar", "precio": 80},
    {"nombre": "sal", "precio": 30, "stock": 0}
]

for producto in productos:
    print(reporte_producto(producto))