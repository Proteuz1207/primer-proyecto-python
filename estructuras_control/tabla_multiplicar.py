# Script para generar la tabla de multiplicar de un número
# Aprendiendo el uso del bucle 'for' en Python

numero = 7  

print(f"=== Tabla del {numero} ===")

# El bucle for recorre del 1 al 10 (el 11 es el límite exclusivo)
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")