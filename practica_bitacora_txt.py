def mostrar_menu():
    print("\n1. Registrar nueva actividad")
    print("2. Ver historial completo")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elija una opción (1-3):\n").strip()

    if opcion == "1":
        actividad = input("Ingresa la nueva actividad:\n").strip()
        if actividad == "":
            print("La actividad no puede estar vacía")
        else:
            with open("/tmp/bitacora.txt", "a", encoding="utf-8") as archivo:
                archivo.write(actividad + "\n")
            print("Actividad guardada en bitacora.txt")

    elif opcion == "2":
        try:
            with open("/tmp/bitacora.txt", "r", encoding="utf-8") as archivo:
                print("\n--- HISTORIAL DE BITÁCORA ---")
                print(archivo.read())
        except FileNotFoundError:
            print("Aún no hay actividades guardadas.")

    elif opcion == "3":
        print("Cerrando bitácora, tus actividades quedaron guardadas")
        break

    else:
        print("Opción inválida: por favor elija 1, 2 o 3.")
      
