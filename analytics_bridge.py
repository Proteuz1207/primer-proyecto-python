import pandas as pd

# 1. Creamos la misma tabla de datos (en Python se llama DataFrame)
datos = {
    'ID_Ventas': ['V001', 'V002', 'V003'],
    'Provincia': ['Santo Domingo Oeste', 'Santiago', 'La Romana'],
    'Monto_Bruto': [150000, 280000, 120000]
}

df = pd.DataFrame(datos)

# 2. RETO 1: Calcular el ITBIS (Usamos la coma decimal en Python con un punto '.' por sintaxis de código)
df['Sum of ITBIS'] = df['Monto_Bruto'] * 0.18

# 3. RETO 2: Calcular el Neto (Monto_Bruto menos ITBIS)
df['Sum of Neto'] = df['Monto_Bruto'] - df['Sum of ITBIS']

# 4. RETO 3: Mostrar el resumen gerencial en la terminal
print("--- REPORTE DE VENTAS PROCESADO ---")
print(df[['ID_Ventas', 'Provincia', 'Sum of ITBIS', 'Sum of Neto']])