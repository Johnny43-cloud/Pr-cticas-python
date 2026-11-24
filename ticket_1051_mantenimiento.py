import json 

ARCHIVO = "/tmp/mantenimiento.json"
def cargar_datos():
    try:
        with open(ARCHIVO,"r",encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        return [] 
  
def guardar_datos(registros):
    with open(ARCHIVO,"w",encoding="utf-8") as f:
        json.dump(registros,f, indent=4, ensure_ascii=False)
      
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("⚠️El campo no puede estar vacío")
        else:
            return texto
          
def pedir_float_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("⚠️El monto debe ser mayor a 0")
        except ValueError:
            print("⚠️Error: Ingrese una cantidad válida")
          
def pedir_opcion_tipo():
    while True:
        print("Tipo de equipo")
        print("1. Moto/auto")
        print("2. PC/laptop")
        opcion = input("Elije una opcion (1-2):\n").strip()

        if opcion == "1":
            return "vehículo" 
        elif opcion == "2":
            return "computadora"
        else:
            print("opcion inválida. Elige 1 o 2 ")

registros = cargar_datos()

while True:
    print("\n1. Registrar mantenimiento")
    print("2. Listar mantenimientos")
    print("3. Marcar mantenimiento como realizado")
    print("4. Resumen de costos y pendientes") 
    print("5. Salir")
    opcion = input("Elige una opcion (1-5):\n").strip()
    if opcion == "1":
        tipo = pedir_opcion_tipo()
        equipo = pedir_texto("Nombre del equipo o vehículo:\n")
        tarea = pedir_texto("Mantenimiento a realizar:\n")
        costo = pedir_float_positivo("Costo estimado ($):\n")
        registro = {"tipo":tipo ,"equipo": equipo, "tarea":tarea , "costo": costo, "completado": False}
        registros.append(registro)
        guardar_datos(registros)
        print(" Datos registrados exitosamente")
      
    elif opcion == "2":
        if len(registros) == 0:
            print("No hay registros")
        else:
            print("\n --- LISTA DE REGISTROS ---")
        for i, registro in  enumerate(registros,start=1):
            if registro["completado"]:
                estado = "[x]"
            else:
                estado = "[ ]"
                print(f"{i}. {estado} {registro['tipo']} | {registro['equipo']} | {registro['tarea']} | {registro['costo']:.2f}")
              
    elif opcion == "3":
        if len(registros) == 0:
            print("No hay registros")
        else:
            for i, registro in enumerate(registros, start=1):
                if registro["completado"]:
                    estado = "[x]"
                else:
                    estado = "[ ]"
                    print(f"{i}. {estado} {registro['tipo']} | {registro['equipo']} | {registro['tarea']} | {registro['costo']:.2f}")
        try:
            num = int(input("Numero de mantenimiento a completar:\n"))
            if 1 <= num <= len(registros):
                registros[num - 1]["completado"]=True
                guardar_datos(registros)
                print("Mantenimiento marcado como realizado")
            else:
                print("Número fuera de rango")
        except ValueError:
            print("Debes ingresar un número válido")
          
    elif opcion == "4":
        if len(registros) == 0:
            print("No hay datos para calcular")
        else:
            total_invertido = sum(r["costo"]for r in registros)
            total_realizado = sum(r["costo"]for r in registros if r ["completado"])
            pendientes = sum(1 for r in registros if not r["completado"])
            print(f"total invertido: ${total_invertido:.2f}")
            print(f"total realizado: ${total_realizado:.2f}")
            print(f"Mantenimientos pendientes: {pendientes}")
    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opcion inválida. Elige entre 1 y 5.")
            
      
























          
        
