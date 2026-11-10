# =====================================================================
# RETO RELÁMPAGO NOCTURNO: CONVERSOR DE VELOCIDAD (M/S A KM/H)
# =====================================================================

# PASO 1: Pide la velocidad en metros por segundo (m/s) usando float(input(...))
# (Guárdalo en una variable llamada 'velocidad_ms')
velocidad_ms = float(input("¿Cuál es la velocidad en m/s?:\n"))
# PASO 2: Multiplica 'velocidad_ms' por 3.6 para convertirla a km/h
# (Guárdalo en una variable llamada 'velocidad_kmh')
velocidad_kmh = velocidad_ms * 3.6
# PASO 3: Usa if / elif / else para clasificar la velocidad:
# - Si 'velocidad_kmh' es mayor a 100: imprime "⚠️ ¡Exceso de velocidad!" con round(velocidad_kmh, 1)
# - elif 'velocidad_kmh' es mayor o igual a 60: imprime "✅ Velocidad normal en carretera" con round(velocidad_kmh, 1)
# - else: imprime "🐢 Velocidad baja en ciudad" con round(velocidad_kmh, 1)
if velocidad_kmh > 100:
    print(f"⚠️¡Exceso de velocidad!⚠️: {round(velocidad_kmh, 1)} km/h")
elif velocidad_kmh >= 60:
    print(f"✔️ Velocidad normal en carretera: {round(velocidad_kmh, 1)} km/h")
else:
    print(f"🐢Velocidad baja en ciudad:{round(velocidad_kmh, 1)} km/h")
  
