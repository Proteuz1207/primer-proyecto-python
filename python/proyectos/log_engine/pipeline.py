# ==============================================================================
# PROYECTO: LogEngine - Módulo de Tubería de Datos (Pipeline)
# OBJETIVO: Procesar flujos de datos entrantes con validación de estado central
# ==============================================================================

# 1. Variables de Control de Infraestructura
paquete_datos = [12, 45, 85, 30]
sistema_operativo_ok = True  # Modifica a False para verificar el bloqueo de memoria

print("=== LOGENGINE: Iniciando Extracción de Métricas ===")

# 2. Filtro de Seguridad Perimetral: Si está apagado, no gastamos ciclos de procesamiento
if not sistema_operativo_ok:
    print("🛑 ERROR CRÍTICO: El sistema central está desconectado. Proceso abortado.")

else:
    print("✅ Conexión establecida. Procesando lote de registros...")
    print("-" * 50)
    
    # El bucle FOR se ejecuta de forma segura sabiendo que el sistema responde
    for registro in paquete_datos:
        if registro >= 80:
            print(f"🚨 ALERTA DE CARGA: Registro {registro}% excede el umbral seguro.")
        else:
            print(f"🟢 ESTADO NORMAL: Registro {registro}% validado correctamente.")
            
    print("-" * 50)
    print("🏁 Pipeline finalizado con éxito.")