# =====================================================================
# PRÁCTICA 1: SIMULADOR DE ACCESO A SERVIDOR CRÍTICO (INFOSEC)
# OBJETIVO: Validar credenciales y bloquear el sistema tras 3 fallos
# =====================================================================

# PASO 1: Crea la variable con la contraseña del servidor (ej. "admin123")
contraseña_servidor = "macho18"
# PASO 2: Crea la variable para los intentos máximos permitidos (ej. empieza en 3)
intentos_disponibles = 3
# PASO 3: Crea una variable booleana para saber si el acceso fue concedido (ej. empieza en False)
acceso_concedido = False
# ---------------------------------------------------------------------
# INICIO DEL BUCLE DE SEGURIDAD (Se repite mientras queden intentos y no se haya concedido acceso)
# ---------------------------------------------------------------------

# PASO 4: Escribe el bucle 'while' que evalúe si los intentos son mayores que 0
# Y ADEMÁS que la variable de acceso concedido siga siendo False
while intentos_disponibles > 0 and acceso_concedido == False:
    # PASO 5: Muestra en pantalla un mensaje indicando cuántos intentos le quedan al usuario
    print(f"¡Atención!, te quedan {intentos_disponibles} intentos")
    # PASO 6: Pide la contraseña al usuario con input() y límpiala con tus dos escudos (.lower().strip())
    contraseña_usuario = input("Tu contraseña es:").lower().strip()
    # PASO 7: Crea la condición 'if' para verificar si la contraseña del usuario coincide con la del paso 1
   # (¡Aquí puedes usar el operador 'or' por si quieres aceptar una contraseña alternativa, ej: "root"!)
    if contraseña_usuario == contraseña_servidor or contraseña_servidor == "root":
        # PASO 8 (Dentro del if): Si acertó, cambia la variable de acceso concedido a True
        # Muestra un mensaje épico en verde o con iconos diciendo "CONEXIÓN ESTABLECIDA"
        acceso_concedido = True
        print("🔓¡CONEXION ESTABLECIDA!, Muy bien hecho usuario lo lograste")
    # PASO 9: Crea el 'else' en caso de que la contraseña sea incorrecta
     else: 
        print("🔒¡Contraseña incorrecta!")
        # PASO 10 (Dentro del else): Resta un intento a la variable (intentos = intentos - 1)
        # Muestra un mensaje de advertencia diciendo "CREDENCIALES INCORRECTAS"
        intentos_disponibles = intentos_disponibles -1
        print(f"te quedan{intentos_disponibles} intentos, ❌ !CREDENCIALES INCORRECTAS❌")
# ---------------------------------------------------------------------
# FIN DE LA VERIFICACIÓN (Fuera del bucle while, el sistema evalúa el estado final)
# ---------------------------------------------------------------------

# PASO 11: Crea un 'if' final para evaluar si el acceso concedido es True
if acceso_concedido == True:
    # PASO 12 (Dentro del if): Muestra un reporte final limpio que diga "Bienvenido al sistema seguro."
    print("🍷¡BIENVENIDO AL SISTEMA SEGURO!🍷")
# PASO 13: Crea el 'else' (significa que se quedó sin intentos y el acceso sigue en False)
else:
    # PASO 14 (Dentro del else): Muestra un mensaje de alerta máxima: "SISTEMA BLOQUEADO. REPORTANDO IP."
    print("☢️¡Alerta maxima!:SISTEMA BLOQUEADO. REPORTANDO IP.☢️")
# =====================================================================
# FIN DE LA PLANTILLA - ¡Tómate tu tiempo y hazlo todo de un solo tirón!
# =====================================================================
