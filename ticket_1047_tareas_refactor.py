import json
try:
    with open("/tmp/tareas.json","r",encoding="utf-8") as archivo:
        tareas = json.load(archivo)
except (FileNotFoundError , json.JSONDecodeError):
    tareas = []
def guardar_tareas(tareas):
    with open("/tmp/tareas.json","w",encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)
def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print(" No hay tareas registradas")
        return False
    else:
        print("\n --- LISTAS DE TAREAS ---")
        for i, tarea in enumerate(tareas, start=1):
            if tarea.get("comoletada", False):
                estado = "[x]"
            else:
                estado = "[]"
                print(f"{i}.{estado} {tarea['descripcion']} (prioridad: {tarea['prioridad']})")
        return True
def mostrar_menu():
    print("\n1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Filtrar por prioridad")
    print("6. Salir")
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("⚠️ El campo no puede estar vacío")
        else:
            return texto
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("⚠️Error: La cantidad debe ser mayor a 0")
        except ValueError:
            print("⚠️Error: Ingrese una cantidad válida ")
while True:
    mostrar_menu()
    opcion = input("Elija una opcion (1,2,3,4,5 o 6):\n").strip()
    if opcion == "1":
        descripcion = pedir_texto("Ingresa la descripcion de la tarea:\n")
        prioridad = pedir_texto("Ingresa la prioridad (alta, media o baja):\n")
        tarea = {"descripcion": descripcion, "prioridad": prioridad, "completada": False}
        tareas.append(tarea)
        guardar_tareas(tareas)
    elif opcion == "2":
        mostrar_tareas(tareas)
    elif opcion == "3":
        if mostrar_tareas(tareas):
            num = pedir_entero("Ingrese el número de la tarea a completar:\n")
            if 1<= num <= len(tareas):
                tareas[num - 1]["completada"] = True
                guardar_tareas(tareas)
                print("Tarea marcada como completada")
            else:
                print("⚠️Error: El número no existe")
    elif opcion == "4":
        if mostrar_tareas(tareas):
            num = pedir_entero("Ingrese el número de la tarea a eliminar:\n")
            if 1<= num <= len(tareas):
                tareas.pop(num - 1)
                guardar_tareas(tareas)
                print("Tarea eliminada exitosamente")
            else:
                print("⚠️Error: El número no existe")
    elif opcion == "5":
        prio = pedir_texto("Ingrese prioridad a filtrar (alta/media/baja):\n").lower()
        filtradas = [t for t in tareas if t["prioridad"].lower == prio]
        mostrar_tareas(filtradas)
    elif opcion == "6":
        print("¡Hasta luego! Tareas guardadas en /tmp/tareas.json")
        break
    else:
        print("⚠️ Opción no válida. Elije 1,2,3,4,5 o 6")
      





















          

