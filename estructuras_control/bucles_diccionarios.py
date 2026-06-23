# Script General: Recorrido Avanzado de Diccionarios con For
# Explorando los métodos nativos .keys(), .values() y .items()

# 1. Definición de nuestro diccionario base
metricas_sistema = {
    "servicio": "Procesador Central",
    "version": 2.5,
    "consumo_ram": 78,
    "estado_critico": False
}

print("=== MÉTODO 1: Recorrer solo las CLAVES (.keys()) ===")
for etiqueta in metricas_sistema.keys():
    print(f"🔑 Nombre del parámetro: {etiqueta}")

print("\n=== MÉTODO 2: Recorrer solo los VALORES (.values()) ===")
for dato in metricas_sistema.values():
    print(f"📊 Valor registrado: {dato}")

print("\n=== MÉTODO 3: El Rey de los Datos - CLAVE y VALOR (.items()) ===")
for parametro, valor in metricas_sistema.items():
    print(f"⚙️ Parámetro: {parametro:<15} | Estado Actual: {valor}")