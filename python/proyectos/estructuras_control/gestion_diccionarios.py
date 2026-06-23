# Script General: Modelado de Datos con Diccionarios
# Uso de la sintaxis de llaves {} para almacenar datos estructurados

servidor_config = {
    "identificador": "SRV-ROJO-01",
    "ip_acceso": "192.168.1.50",
    "carga_porcentaje": 62.8,
    "en_linea": True
}

print("=== Estructura Completa del Diccionario ===")
print(servidor_config)
print("------------------------------------------------")

nombre_nodo = servidor_config["identificador"]
estado_actual = servidor_config["en_linea"]

print(f"📡 Monitoreando Nodo: {nombre_nodo}")
print(f"🔌 Estado del Interruptor: {estado_actual}")
print("------------------------------------------------")

servidor_config["carga_porcentaje"] = 94.1

print("⚠️ ACTUALIZACIÓN DE CARGA EN PANTALLA:")
print(f"La nueva carga del {servidor_config['identificador']} es de: {servidor_config['carga_porcentaje']}%")