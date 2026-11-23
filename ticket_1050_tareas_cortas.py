tareas = []
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("⚠️El campo no puede estar vacío")
        else:
            return texto
while True:
    print("\n1. Agregar tarea")
    print("2. Ver tareas y resumen")
    print("3. Completar tarea")
    print("4. Salir")
    opcion = input("Elije una opcion (1-4):\n").strip()
    if opcion == "1":
        titulo = pedir_texto("Ingrese el nombre de la tarea:\n")
        tarea = {"titulo": titulo, "completada" : False}
        tareas.append(tarea)
        print("Tarea guardada exitosamente")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas")
        else:
            print("\n --- LISTAS DE TAREAS ---")
        for i, tarea in enumerate(tareas, start=1):
            if tarea["completada"]:
                estado = "[x]"
            else:
                estado = "[]"
                print(f"{i}. {estado} {tarea['titulo']}")
                pendientes = sum(1 for t in tareas if not t["completada"])
                print(f"tareas pendiente: {pendientes}")
    elif opcion == "3":
        if not tareas:
            print("No hay tareas para completar")
        else:
            for i, tarea in enumerate(tareas, start=1):
                 if tarea ["completada"]:
                     estado = "[x]"
                 else:
                     estado = "[]"
                     print(f"{i}. {tarea['titulo']}")
            try: 
                num = int(input("Numero de tarea a completar:\n"))
                if 1 <= num <= len(tareas):
                    tareas[num - 1]["completada"]= True
                    print("tarea marcada como completada")
                else:
                    print("⚠️Error: Número fuera de rango")
            except ValueError:
                print("Debes ingresar un número válido")
    elif opcion == "4":
        print("Saliendo del sistema ¡Hasta luego!")
        break 



                  
      
            
