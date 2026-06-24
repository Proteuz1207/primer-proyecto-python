# ==============================================================================
# PROYECTO: LogEngine - Módulo de Tubería de Datos (Pipeline)
# OBJETIVO: Procesar flujos de datos entrantes con validación de estado central
# ==============================================================================

# 1. Variables de Control de Infraestructura
lote_servidores = [
    {"id": "SRV-ALFA",  "consumo_cpu": 45, "zona": "Santo Domingo"},
    {"id": "SRV-BETA",  "consumo_cpu": 88, "zona": "Santiago"},
    {"id": "SRV-GAMMA", "consumo_cpu": 92, "zona": "Santo Domingo Oeste"},
    {"id": "SRV-DELTA", "consumo_cpu": 15, "zona": "La Romana"}
]
sistema_operativo_ok = True  # Modifica a False para verificar el bloqueo de memoria

print("=== LOGENGINE: Iniciando Extracción de Métricas ===")

# 2. Filtro de Seguridad Perimetral: Si está apagado, no gastamos ciclos de procesamiento
if not sistema_operativo_ok:
    print("🛑 ERROR CRÍTICO: El sistema central está desconectado. Proceso abortado.")

else:
    print("✅ Conexión establecida. Procesando lote de registros...")
    print("-" * 50)
    
    # El bucle FOR se ejecuta de forma segura sabiendo que el sistema responde
    for registro in lote_servidores:
        codigo_id = registro["id"]
        carga_cpu = registro["consumo_cpu"]
        ubicacion = registro["zona"]

        # 4. Lógica de Negocio (Evaluación de alertas en base a los datos extraídos)
        
        if carga_cpu >= 80:
            estado_visual = f"🚨 ALERTA CRÍTICA: {carga_cpu}% CPU"
        else:
            estado_visual = f"🟢 ESTADO ESTABLE: {carga_cpu}% CPU"
            
        # 5. Formateo limpio en pantalla usando alineación de espacios
        print(f"🖥️ Nodo: {codigo_id:<12} | Ubicación: {ubicacion:<20} | {estado_visual}")
        
    print("=" * 65)
    print("🏁 Pipeline de procesamiento finalizado correctamente.")
        





