# =====================================================================
# PRÁCTICA 4: CIRCUITO DE CARRERAS Y APUESTAS (LISTAS + WHILE)
# =====================================================================

# PASO 1: Crea una lista llamada 'autos_pista' con 3 autos iniciales:
# ["nissan gtr", "toyota supra", "mazda rx7"]
autos_pista = ["nissan gtr", "toyota supra", "mercedes benz"]

# PASO 2: Crea dos variables iniciales:
# - 'saldo' = 500.0
# - 'carreras_ganadas' = 0
saldo = 500.0
carreras_ganadas = 0

# PASO 3: Inicia un bucle infinito con 'while True:' para mantener el torneo activo:
while True:
    # PASO 4: Si 'saldo' es menor o igual a 0, imprime "💸 ¡Te quedaste sin fondos! Fin del torneo."
    # y usa 'break' para terminar el juego.
    if saldo <= 0: 
        print("💸¡Te quedaste sin fondos! Fin del torneo")
        break
    # PASO 5: Imprime tu saldo actual (con round) y un menú con 4 opciones:
    # 1. Ver autos en la pista
    # 2. Inscribir un auto nuevo
    # 3. Retirar un auto por falla mecánica
    # 4. Apostar en la carrera
    # 5. Retirarse del circuito (Salir)
    print(f"💰saldo actual : {round(saldo, 2)}")
    print(" 1. Ver autos en la pista")
    print(" 2. Inscribir un auto nuevo")
    print(" 3. Retirar un auto por falla mecánica")
    print(" 4. Apostar en la carrera")
    print(" 5. Retirarse del circuito")
    # PASO 6: Pide al usuario que elija una opción (1 a 5) con input().strip()
    # y guárdala en una variable llamada 'opcion'.
    opcion = input(" Elije una opcion: (1-5)\n").strip()

    # PASO 7: Evalúa 'opcion' con if / elif / else:
    # - Si opcion == "1":
    #       Imprime cuántos autos hay compitiendo usando len(autos_pista)
    #       y usa un bucle 'for auto in autos_pista:' para mostrar cada auto en pantalla.
    if opcion == "1":
        print(f"🏎️ Autos en pista: {(len(autos_pista))}: ")
        for auto in autos_pista:
          print(f" - {auto}")
    # - elif opcion == "2":
    #       Pide el nombre del auto nuevo con input().lower().strip()
    #       Usa autos_pista.append(nuevo_auto) para meterlo a la pista
    #       e imprime un mensaje confirmando la inscripción.
    elif opcion == "2":
        nuevo_auto = input("Nombre del auto nuevo:\n").lower().strip()
        autos_pista.append(nuevo_auto)
        print(f"¡{nuevo_auto} inscrito en la pista! ")
    # - elif opcion == "3":
    #       Pide el nombre del auto a retirar con input().lower().strip()
    #       Usa 'if auto_retirar in autos_pista:' para verificar:
    #           - Si está: usa autos_pista.remove(auto_retirar) e imprime "🔧 Auto retirado a talleres."
    #           - else: imprime "❌ Ese auto no está en la pista."
    elif opcion == "3":
        auto_retirar = input("Nombre del auto que retira:\n").lower().strip()
        if auto_retirar in autos_pista:
             autos_pista.remove(auto_retirar)
             print("🔧 Auto retirado a talleres")
        else:
            print("❌ Ese auto no esta en la pista")
    # - elif opcion == "4":
    #       Pide por qué auto apuesta con input().lower().strip()
    #       Verifica con 'if auto_apuesta in autos_pista:' si el auto existe:
    #           - Si existe: pide cuánto dinero apuesta con float(input(...))
    #               - Si apuesta > saldo o apuesta <= 0:
    #                     imprime "⚠️ Apuesta inválida o saldo insuficiente."
    #               - else:
    #                     Pregunta si el auto quedó en primer lugar:
    #                     resultado = input("¿Tu auto ganó la carrera? (si/no)\n").lower().strip()
    #                     - Si resultado == "si":
    #                           suma 'apuesta' a 'saldo', suma 1 a 'carreras_ganadas'
    #                           e imprime f"🏆 ¡GANASTE! Nuevo saldo: ${round(saldo, 2)}"
    #                     - else:
    #                           resta 'apuesta' a 'saldo'
    #                           e imprime f"💥 Perdiste la apuesta. Nuevo saldo: ${round(saldo, 2)}"
    #           - else:
    #               imprime "❌ Ese auto no está inscrito en la carrera."
    elif opcion == "4":
        apuesta_auto = input("¿Por qué auto apuesta?:\n").lower().strip()
        if apuesta_auto in autos_pista:
          try:
            apuesta = float(input("¿cuánto dinero apuestas?:\n"))
          except valueError:
            print("escribe solo números ")
            continue 
            if apuesta > saldo or apuesta <= 0:
                print("⚠️Apuesta inválida o saldo insuficiente")
            else:
                resultado = input("¿Tu auto ganó la carrera?: (si/no)\n").lower().strip()
                if resultado == "si" or resultado == "sí":
                    saldo += apuesta
                    carreras_ganadas += 1
                    print(f"🏆 ¡GANASTE! nuevo saldo: ${round(saldo, 2)}")
                else:
                    saldo -= apuesta
                    print(f"💥 Perdiste la apuesta. Nuevo saldo: ${round(saldo,2)}")
        else:
            print("❌ responde si o no")
    # - elif opcion == "5":
    #       Imprime tu resumen final: saldo final (con round) y carreras ganadas, y usa 'break'.
    elif opcion == "5":
        print(f" Saldo final: ${round(saldo, 2)}| carreras ganadas: {carreras_ganadas}")
        break
    # - else:
    #       Imprime "⚠️ Opción incorrecta. Elige del 1 al 5."
    else:
        print("⚠️ Opción incorrecta. Elige (1-5)")






      
