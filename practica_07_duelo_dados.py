# =====================================================================
# PRÁCTICA 7: DUELO DE DADOS EN EL CASINO (RANDOM + TRY/EXCEPT)
# =====================================================================

# PASO 1: En la primera línea de código, importa la librería de azar escribiendo:
# import random
import random

# PASO 2: Usa un bucle 'while True:' para pedir el nombre del jugador hasta que sea válido:
# - Pide: nombre = input("Ingresa tu nombre de jugador (solo letras):\n").strip()
# - Revisa con 'if nombre.isalpha():' -> imprime un saludo de bienvenida y usa 'break'.
# - En el 'else:' -> imprime "⚠️ Error: Escribe solo letras, sin números ni espacios."
while True:
    nombre = input("jhon mclane:\n").strip()
    if nombre.isalpha():
        print("🗣️ ¡Bienvenido AL JUEGO DE DADOS EN EL CASINO")
        break
    else:
        print("⚠️Error: Escribe solo letras, sin números ni espacios")
# PASO 3: Crea las variables iniciales del juego (pegadas al borde izquierdo):
# - 'saldo' = 300.0
# - 'rondas_ganadas' = 0
saldo = 300.0
rondas_ganadas = 0
# PASO 4: Inicia el bucle principal del casino con 'while True:':
while True:
    # PASO 5: Si 'saldo' es menor o igual a 0, imprime "💸 Te quedaste en cero. Fin del juego." y usa 'break'.
    if saldo <= 0:
        print("💸 Te quedaste en cero.Fin del juego")
        break

    # PASO 6: Muestra el saldo actual (con round) y pregunta si quiere jugar o retirarse:
    # decision = input(f"\n💰 Saldo: ${round(saldo, 2)} | ¿Quieres lanzar los dados? (si/no):\n").lower().strip()    
    decision = input(f"\n💰 saldo: ${round(saldo, 2)} | ¿Quieres lanzar los dados? (si/no):\n").lower().strip()

    # PASO 7: Evalúa 'decision' con if / elif / else:
    # - Si decision == "no":
    #       Imprime el resumen final (nombre, saldo final con round y rondas_ganadas) y usa 'break'.
    if decision == "no":
        print(f"\n💰 {nombre} | saldo final: ${round(saldo, 2)} | rondas_ganadas: {rondas_ganadas}")
        break 
    # - elif decision == "si" or decision == "sí":
    #       Usa un bloque 'try:' para pedir la apuesta de forma segura:
    #           apuesta = float(input("¿Cuánto dinero apuestas?:\n"))
    #       Debajo, a la misma altura de 'try:', pon 'except ValueError:':
    #           imprime "⚠️ Error: Debes escribir un número válido."
    #           usa 'continue' (para volver al inicio del menú del casino)
    elif decision == "si" or decision == "sí":
        try:
            apuesta = float(input("¿cuánto dinero apuestas?:\n"))
        except ValueError:
            print("⚠️ Error: desde escribir un número válido.")
            continue 
            
    #       (Afuera del try/except, pero adentro del elif):
    #       Revisa 'if apuesta > saldo or apuesta <= 0:' -> imprime "⚠️ Apuesta inválida o saldo insuficiente."
    #       En el 'else:':
    #           1. Genera dos números al azar del 1 al 6 usando random.randint(1, 6):
    #              dado_jugador = random.randint(1, 6)
    #              dado_banca = random.randint(1, 6)
    #           2. Imprime ambos resultados en pantalla.
    #           3. Compara los dados con if / elif / else:
    #              - Si dado_jugador > dado_banca: suma 'apuesta' a 'saldo', suma 1 a 'rondas_ganadas' y celebra.
    #              - elif dado_jugador < dado_banca: resta 'apuesta' a 'saldo' y avisa que ganó la banca.
    #              - else: imprime "🤝 ¡Empate! Recuperas tu apuesta."
        if apuesta > saldo or apuesta <= 0:
            print("⚠️ Apuesta inválida o saldo insuficiente.")
        else:
            dado_jugador = random.randint(1 , 6)
            dado_banca = random.randint(1 , 6)  
            print(f"Tu dado: {dado_jugador} | dado banca: {dado_banca}")
            if dado_jugador > dado_banca:
                saldo += apuesta
                rondas_ganadas += 1
                print("¡Felicidades Ganaste!")
            elif dado_jugador < dado_banca:
                saldo -= apuesta
                print("💥¡Ganaste la banca!")
            else:
                print("🤝¡Empate! Recuperas tu apuesta.")
    # - else:
    #       Imprime "⚠️ Responde solo 'si' o 'no'."
else:
    print("⚠️Responde solo (si/no).")



