# Script de Práctica: Extracción en Estructuras Anidadas

# Una LISTA [] que contiene tres DICCIONARIOS {} adentro, separados por comas
servidores_red = [
    {"nombre": "Servidor-Alfa", "ip": "10.0.01", "status": "OK"},
    {"nombre": "Servidor-Beta", "ip": "10.0.02", "status": "FALLO"},
    {"nombre": "Servidor-Gama", "ip": "10.0.03", "status": "OK"}

]

print("=== Extraccion Quirurgica en Memoria ===")

# Paso 1: Ir al primer cajón de la lista (Índice 0)

primer_servidor = servidores_red[0]
print(f"Contenido del cajón 0: {primer_servidor}")

# Paso 2: Ir al primer cajón de la lista Y extraer directamente una etiqueta del diccionario
nombre_del_segundo = servidores_red[1]["nombre"]
status_del_segundo = servidores_red[1]["status"]
print(f"El componente en el índice 1 es: {nombre_del_segundo} y su estado es: {status_del_segundo}")

print("\n=== AUTOMATIZACIÓN MASIVA CON BUCE FOR ===")

# La variable temporal 'servidor' va a tomar UN DICCIONARIO COMPLETO en cada vuelta
for servidor in servidores_red:
    # Dentro del bucle, 'servidor' actúa como el diccionario de la vuelta actual
    nombre = servidor["nombre"]
    ip_srv = servidor["ip"]
    estado = servidor["status"]
    # Imprimimos de forma estructurada los datos de cada uno
    print(f"🖥️ {nombre:<15} | IP: {ip_srv:<10} | Estado: {estado}")
