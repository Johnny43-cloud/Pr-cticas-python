# =====================================================================
# PRÁCTICA 2: SIMULADOR DE CAJERO AUTOMÁTICO (ATM)
# OBJETIVO: Gestionar saldo bancario, validar retiros y evitar sobregiros
# =====================================================================

# PASO 1: Crea una variable con el saldo inicial de la cuenta (ej. 1500.50)
saldo_inicial = 1900.25
# PASO 2: Crea una variable booleana llamada 'sesion_activa' que empiece en True
sesion_activa = True
# ---------------------------------------------------------------------
# INICIO DEL BUCLE DEL CAJERO (Se repite mientras 'sesion_activa' sea True)
# ---------------------------------------------------------------------

# PASO 3: Escribe el bucle 'while' que evalúe si 'sesion_activa' es True
while sesion_activa == True: 
    # PASO 4: Muestra en pantalla el saldo actual usando round(saldo, 2) para que siempre tenga máximo 2 decimales
    print(f"Tu saldo actual es : ${round(saldo_inicial, 2)}")
    # PASO 5: Pide al usuario que elija una opción: "retirar", "depositar" o "salir"
    # (Recuerda usar tus dos escudos: .lower().strip())
    elegir_opcion = input ("¿Qué desea usted?:'retirar' ,'depositar', 'salir': \n").lower().strip()
    # PASO 6: Crea un 'if' para verificar si el usuario escribió "salir" (o usa 'or' para aceptar también "s")
    if elegir_opcion == "salir" or elegir_opcion == "s":
        # PASO 7 (Dentro del if): Cambia 'sesion_activa' a False y muestra un mensaje de despedida
        sesion_activa = False
        print("¡Gracias por utilizar el cajero, vuelva pronto!")
    # PASO 8: Crea un 'elif' para verificar si el usuario escribió "depositar" (o "d")
    elif elegir_opcion == "depositar" or elegir_opcion == "d":
        # PASO 9 (Dentro del elif): Pide cuánto dinero quiere depositar y conviértelo a decimal con float(input(...))
        monto = float(input("¿Cuánto dinero desea depositar: "))
        # PASO 10: Valida con un 'if' interno que el monto sea mayor a 0
        # Si es válido, súmalo al saldo y muestra el nuevo saldo redondeado
        # Si es 0 o negativo, muestra un error ("Monto inválido")
        if monto > 0 :
              print(f"{monto} + {saldo_inicial}: ${round(saldo_inicial)}")
        if monto == "0" or "negativo":
              print("Monto inválido")
    # PASO 11: Crea otro 'elif' para verificar si el usuario escribió "retirar" (o "r")
    elif elegir_opcion == "retirar" or elegir_opcion == "r":
        # PASO 12 (Dentro del elif): Pide cuánto dinero quiere retirar y conviértelo a decimal con float(input(...))
        monto = float(input("¿Cuantos dinero desea retirar: "))
        # PASO 13: Valida con 'if / elif / else' internos:
        # - Si el monto es menor o igual a 0: muestra "Monto inválido"
        # - Si el monto es mayor al saldo disponible: muestra "Fondos insuficientes"
        # - Si todo está bien (else): resta el monto al saldo y muestra "Retiro exitoso" con el saldo restante
        if monto <= 0:
          print("Monto inválido")
        elif monto > saldo_inicial:
          print("Fondos insuficiente")
        else:
          saldo_inicial = saldo_inicial - monto
          print(f"Retiro exitoso. saldo restante :{round(saldo_inicial,2)}")
    # PASO 14: Crea un 'else' final (por si el usuario escribe una opción que no existe)
    else: 
        # PASO 15 (Dentro del else): Muestra "Opción no reconocida. Intenta de nuevo."
        print("Opción no reconocida. Intenta de nuevo")
# ---------------------------------------------------------------------
# FIN DEL PROGRAMA (Fuera del bucle while)
# ---------------------------------------------------------------------

# PASO 16: Muestra un resumen final con el saldo con el que cerró la cuenta
        print(f"Sesion cerrada. Tu saldo final es : {round(saldo_inicial,2)}")
      
