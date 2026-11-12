# =====================================================================
# PRÁCTICA 8: GESTOR DE LISTA DE COMPRAS (LISTAS + BUCLE FOR)
# =====================================================================

# PASO 1: Crea una lista vacía llamada 'carrito' pegada al borde izquierdo:
# carrito = []
carrito = [""]

# PASO 2: Inicia el bucle principal del menú con 'while True:':
while True:
    # PASO 3: Muestra el menú de opciones:
    # print("\n--- 🛒 MI LISTA DE COMPRAS ---")
    # print("1. Agregar producto")
    # print("2. Ver lista completa")
    # print("3. Eliminar producto")
    # print("4. Salir")
    print("\n --- 🛒 MI LISTA DE COMPRAS---")
    print("1. Agregar producto")
    print("2. Ver lista de completa")
    print("3. Eliminar producto")
    print("4. Salir")
    # PASO 4: Pide al usuario que elija una opción (1, 2, 3 o 4):
    # opcion = input("Elige una opción:\n").strip()
    opcion = input("Elige una opcion:\n").strip()
    # PASO 5: Evalúa 'opcion' con if / elif / else:
    if opcion == "1":
    # - Si opcion == "1":
    #       Pide el nombre del producto: producto = input("Escribe el producto a agregar:\n").strip().capitalize()
    #       Si producto == "": imprime "⚠️ No puedes agregar un espacio vacío."
    #       En el else:
    #           Usa carrito.append(producto) para guardarlo en la lista.
    #           Imprime f"✅ '{producto}' agregado al carrito."
        producto = input("Escribe el producto a agregar:\n").strip().capitalize()
        if producto == "":
            print("⚠️ No puedes agregar un espacio vacío.")
        else:
            carrito.append(producto)
            print(f"✔️ {producto} agregado al carrito")
    # - elif opcion == "2":
    #       Revisa si la lista está vacía con: if len(carrito) == 0:
    #           Imprime "📭 Tu lista de compras está vacía."
    #       En el else:
    #           Imprime f"\n📋 Tienes {len(carrito)} producto(s):"
    #           Usa un bucle 'for' para mostrar cada artículo uno debajo del otro:
    #           for item in carrito:
    #               print(f"- {item}")
    elif opcion == "2":
             if len(carrito) == 0:
                 print("🧾Tu lista de compras esta vacia")
             else:
                 print(f"\n📜 Tienes {len(carrito)} producto(s):")
             for item in carrito:
                 print(f"- {item}")
    # - elif opcion == "3":
    #       Pide qué producto quiere borrar: borrar = input("Escribe el nombre del producto a eliminar:\n").strip().capitalize()
    #       Revisa si existe en la lista con: if borrar in carrito:
    #           Usa carrito.remove(borrar) para sacarlo de la lista.
    #           Imprime f"🗑️ '{borrar}' eliminado de la lista."
    #       En el else:
    #           Imprime f"⚠️ '{borrar}' no está en tu lista."
    elif opcion == "3":
        borrar = input("Escribe el nombre del producto a eliminar:\n").strip().capitalize()
        if borrar in carrito:
            carrito.remove(borrar)
            print(f"🚮 {borrar} eliminado de la lista")
        else:
            print(f"⚠️ {borrar} no está es tu lista")
              
    # - elif opcion == "4":
    #       Imprime f"👋 Saliendo... Total de productos guardados: {len(carrito)}"
    #       Usa 'break' para cerrar el programa.
    elif opcion == "4":
        print(f"👋 saliendo | Total de productos guardados: {len(carrito)}")
        break
    # - else:
    #       Imprime "⚠️ Opción inválida. Elige 1, 2, 3 o 4."
else:
    print("⚠️ Opción inválida. Elije 1, 2, 3, o 4.")
