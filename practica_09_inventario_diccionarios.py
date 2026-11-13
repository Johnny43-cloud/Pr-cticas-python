# =====================================================================
# PRÁCTICA 9: INVENTARIO CON PRECIOS (DICCIONARIOS + BUCLE FOR)
# =====================================================================

# PASO 1: Crea un diccionario inicial con 3 productos y sus precios (pegado al borde izquierdo):
# inventario = {
#     "Arroz": 1.50,
#     "Leche": 1.25,
#     "Huevos": 3.75
# }
inventario = {"Arroz": 1.50,"Leche": 1.25,"Huevos": 3.75}

# PASO 2: Inicia el bucle principal del menú con 'while True:':
while True:
    # PASO 3: Muestra las opciones del sistema de inventario:
    # print("\n--- 🏪 SISTEMA DE INVENTARIO ---")
    # print("1. Ver inventario y precios")
    # print("2. Agregar o actualizar producto")
    # print("3. Consultar precio de un producto")
    # print("4. Eliminar producto")
    # print("5. Salir")
    print("\n ---🏭 SISTEMA DE INVENTARIO ---")
    print("1. Ver inventario y precios")
    print("2. Agregar o actualizar producto")
    print("3. Consultar precio de un producto")
    print("4. Eliminar producto")
    print("5. Salir")
    # PASO 4: Pide la opción al usuario:
    # opcion = input("Elige una opción (1-5):\n").strip()
    opcion = input("Elige una opcion (1-5):\n").strip()
    # PASO 5: Evalúa 'opcion' con if / elif / else:
    if opcion == "1":
    # - Si opcion == "1":
    #       Imprime "\n📋 PRODUCTOS EN TIENDA:"
    #       Recorre el diccionario usando .items() para sacar el nombre y el precio a la vez:
    #       for producto, precio in inventario.items():
    #           print(f"- {producto}: ${round(precio, 2)}")
        print("\n🧾 PRODUCTOS EN TIENDA:")
        for producto, precio in inventario.items():
            print(f"- {producto}: ${round(precio, 2)}")
    # - elif opcion == "2":
    #       Pide el nombre del producto: nombre = input("Nombre del producto:\n").strip().capitalize()
    #       Usa un bloque 'try:' para pedir el precio de forma segura:
    #           precio = float(input("Precio del producto ($):\n"))
    #           if precio <= 0:
    #               print("⚠️ Error: El precio debe ser mayor a 0.")
    #           else:
    #               # Así se guarda o actualiza un dato en un diccionario:
    #               inventario[nombre] = precio
    #               print(f"✅ '{nombre}' guardado a ${round(precio, 2)}.")
    #       Debajo, a la misma altura de 'try:', pon 'except ValueError:':
    #           print("⚠️ Error: Debes ingresar un precio numérico válido.")
    elif opcion == "2":
        nombre = input("Nombre del producto:\n").strip().capitalize()
        try:
            precio = float(input("precio del producto ($):\n"))
            if precio<=0:
                print("⚠️Error: El precio debe ser mayor a 0")
            else:
                inventario[nombre] = precio
                print(f"✔️ {nombre}: ${round(precio, 2)}")
        except ValueError:
            print("⚠️ Error: Debes de ingresar un precio númerico válido")      
    # - elif opcion == "3":
    #       Pide el producto a buscar: buscar = input("¿Qué producto buscas?:\n").strip().capitalize()
    #       Revisa si existe en el diccionario con 'if buscar in inventario:':
    #           # Así lees el precio de un producto específico:
    #           print(f"🏷️ El precio de '{buscar}' es: ${round(inventario[buscar], 2)}")
    #       En el 'else:':
    #           print(f"⚠️ '{buscar}' no existe en el inventario.")
    elif opcion == "3":
        buscar = input("¿Qué producto buscas?:\n").strip().capitalize()
        if buscar in inventario:
            print(f"🏷️ El precio de {buscar} es: ${round(inventario[buscar], 2)}")
        else:
            print(f"⚠️ {buscar} no existe en el inventario")
    # - elif opcion == "4":
    #       Pide qué producto eliminar: borrar = input("Producto a eliminar:\n").strip().capitalize()
    #       Revisa 'if borrar in inventario:':
    #           # Así se borra una pareja del diccionario:
    #           del inventario[borrar]
    #           print(f"🗑️ '{borrar}' eliminado del inventario.")
    #       En el 'else:':
    #           print(f"⚠️ '{borrar}' no está en el inventario.")
    elif opcion == "4":
        borrar = input("Producto a eliminar:\n").strip().capitalize()
        if borrar in inventario:
            print(f"🚮 {borrar} elimnado del inventario")
        else :
            print(f"⚠️ {borrar} no esta en el inventario")
    # - elif opcion == "5":
    #       Imprime f"👋 Cerrando inventario... Total de productos registrados: {len(inventario)}"
    #       Usa 'break'
    elif opcion == "5":
        print(f"👋 Cerrando inventario... Total de productos registrados: {len(inventario)}")
        break
    # - else:
    #       Imprime "⚠️ Opción inválida. Elige del 1 al 5."
    else:
            print("⚠️ Opción válida. Elige del 1 al 5")
