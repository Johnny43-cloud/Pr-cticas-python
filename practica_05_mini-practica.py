# =====================================================================
# MINI-PRÁCTICA: ESCUDO ANTI-ERRORES CON TRY Y EXCEPT
# =====================================================================

# PASO 1: Inicia un bucle infinito con while True:
while True:
    # PASO 2: Escribe try:
    try:
        # PASO 3: Pide la edad usando int(input("¿Cuántos años tienes?\n"))
        # y guárdala en una variable llamada 'edad'
        edad = int(input("¿Cuántos años tienes?\n"))
        # PASO 4: Si la línea anterior funcionó, imprime f"✅ Edad registrada: {edad} años"
        # y escribe break para salir del bucle.
        print(f"✔️ Edad registrada: {edad} años")
        break
    # PASO 5: A la misma altura que try:, escribe except ValueError:
    except ValueError:
        # PASO 6: Imprime "⚠️ Error: Escribe solo números enteros (sin letras ni puntos)."
        print("⚠️ Error: 9999")
