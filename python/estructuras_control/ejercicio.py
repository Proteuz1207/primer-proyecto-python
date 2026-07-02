class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def ver_stock(self):
        if self.stock > 0:
            return "disponible"
        else:
            return "no disponible"

    def calcular_precio_final(self, cantidad, impuestos=0.12):
        return (self.precio * cantidad) + (self.precio * cantidad * impuestos)



leche = Producto("Leche", 100, 8)
pan = Producto("Pan", 10, 5)
huevo = Producto("Huevo", 100, 0)

print(leche.ver_stock(), leche.calcular_precio_final())
print(pan.ver_stock(), pan.calcular_precio_final())
print(huevo.ver_stock(), huevo.calcular_precio_final())