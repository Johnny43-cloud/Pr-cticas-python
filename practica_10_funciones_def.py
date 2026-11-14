# =====================================================================
# PRÁCTICA 10: FUNCIONES MODULARES (DEF + RETURN)
# =====================================================================

# --- BLOQUE 1: FABRICAMOS NUESTRAS HERRAMIENTAS (DEF) ---

# PASO 1: Define una función llamada 'mostrar_menu()' (pegada al borde izquierdo):
# def mostrar_menu():
#     print("\n--- 🧮 CALCULADORA MODULAR ---")
#     print("1. Calcular total con IVA (15%)")
#     print("2. Calcular descuento")
#     print("3. Salir")
def mostrar_menu():
    print("\n --- CALCULADORA MODULAR ---")
    print("1. Calcular total con IVA (15%)")
    print("2. Calcular descuento ")
    print("3. Salir")

# PASO 2: Define una función llamada 'pedir_monto(mensaje)' que reciba un texto
# y devuelva un número válido mayor a 0 usando 'return':
# def pedir_monto(mensaje):
#     while True:
#         try:
#             valor = float(input(mensaje))
#             if valor <= 0:
#                 print("⚠️ Error: El monto debe ser mayor a 0.")
#             else:
#                 return valor  # 'return' entrega el número listo y sale de la función
#         except ValueError:
#             print("⚠️ Error: Ingresa un número válido.")
def pedir_monto(mensaje):
    while True: 
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("⚠️ Error: El monto debe ser mayor a 0.")
            else:
                return valor
        except ValueError:
            print("⚠️ Error: Ingresa un número válido")
# --- BLOQUE 2: PROGRAMA PRINCIPAL (DEBAJO DE LOS DEF) ---

# PASO 3: Imprime el título de bienvenida (pegado al borde izquierdo):
# print("=== BIENVENIDO AL SISTEMA DE CÁLCULOS ===")
print(" === BIENVENIDO AL SISTEMA DE CÁLCULOS ===")
# PASO 4: Inicia el bucle principal con 'while True:':
while True:
    # PASO 5: Llama a tu primera función para mostrar el menú:
    # mostrar_menu()
    mostrar_menu()
    # PASO 6: Pide la opción al usuario:
    # opcion = input("Elige una opción (1-3):\n").strip()
    opcion = input("Elige una opcion (1-3):\n").strip()
    # PASO 7: Evalúa 'opcion' con if / elif / else:
    if opcion == "1":
    # - Si opcion == "1":
    #       # Reutiliza tu herramienta 'pedir_monto':
    #       precio = pedir_monto("Ingresa el precio del producto ($):\n")
    #       total_iva = precio * 1.15
    #       print(f"✅ Precio final con IVA (15%): ${total_iva:.2f}")
        pedir_monto
        precio = pedir_monto("Ingresa el precio del producto ($):\n")
        total_iva = precio * 1.15
        print(f"✔️Precio final con IVA (15%): ${total_iva:.2f}")
    # - elif opcion == "2":
    #       # Reutiliza la MISMA herramienta 'pedir_monto' dos veces sin repetir el while True:
    #       precio = pedir_monto("Ingresa el precio original ($):\n")
    #       porcentaje = pedir_monto("Ingresa el porcentaje de descuento (ej. 10):\n")
    #       ahorro = precio * (porcentaje / 100)
    #       final = precio - ahorro
    #       print(f"🏷️ Ahorras ${ahorro:.2f} | Total a pagar: ${final:.2f}")
    elif opcion == "2":
        pedir_monto
        precio = pedir_monto("Ingresa el precio original ($):\n")
        porcentaje = pedir_monto("Ingresa el porcentaje de descuento (ej.10):\n")
        ahorro = precio * (porcentaje/ 100)
        final = precio - ahorro
        print(f"🏷️ Ahorras ${ahorro:.2f} | Total a pagar: ${final:.2f}")
    # - elif opcion == "3":
    #       print("👋 Cerrando calculadora modular...")
    #       break
    elif opcion == "3":
        print("👋 Cerrando calculadora modular...")
        break
    # - else:
    #       print("⚠️ Opción inválida. Elige del 1 al 3.")
    else:
        print("⚠️ Opción inválida, Eluge del 1 al 3.")
