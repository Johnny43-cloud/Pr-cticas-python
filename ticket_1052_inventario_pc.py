import json
ARCHIVO = "/tmp/inventario_pc.json"
def cargar_datos():
    try:
        with open(ARCHIVO,"r",encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        return []

def guardar_datos(inventario):
    with open(ARCHIVO,"w",encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print(" El campo no puede estar vacío")
        else:
            return texto

def pedir_float_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print(" El monto debe ser mayor a 0")
        except ValueError:
            print("⚠️ Error: ingrese una cantidad válida")

def pedir_entero_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("El stock no puede ser negativo (0 o más).")
        except ValueError:
            print("⚠️Error: ingrese un número enteró válido")
          
inventario = cargar_datos()

while True:
    print("\n1. Registrar componentes")
    print("2. Listar inventario completo")
    print("3. Actualizar stock de un componente")
    print("4. Buscar componente y resumen de valor total")
    print("5. Salir")
    opcion = input("Elige una opcion (1-5):\n").strip()

    if opcion == "1":
        nombre = pedir_texto("Nombre del componente a registrar:\n")
        precio = pedir_float_positivo("Precio del componente ($):\n")
        stock = pedir_entero_no_negativo("Ingrese la cantidad en stock:\n")
        item = {"nombre":nombre, "precio":precio, "stock":stock, "completado":False}
        inventario.append(item)
        guardar_datos(inventario)
        print("datos guardados en el inventario exitosamente ")
      
    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay componentes registrados")
        else:
            print(" --- LISTA DEL INVENTARIO ---")
        for i, item in enumerate(inventario,start=1):
            if item["stock"] == 0:
                estado = "[AGOTADO]"
            else:
                estado = "[DISPONIBLE]"
                print(f"{i}.{estado} {item['nombre']} | {item['precio']:.2f} | stock: {item['stock']}")

    elif opcion == "3":
        if len(inventario) == 0:
            print("No hay componentes registrados")
        else:
            for i, item in enumerate(inventario,start=1):
                if item["stock"] == 0:
                    estado = "[AGOTADO]"
                else:
                    estado = "[DISPONIBLE]"
                print(f"{i}.{estado} {item['nombre']} | {item['precio']:.2f} | stock: {item['stock']}")
        try:
            num = int(input("Número del componente a actualizar:\n"))
            if 1 <= num <= len(inventario):
                nuevo_stock = pedir_entero_no_negativo("Nuevo stock:\n")
                inventario[num - 1]["stock"] = nuevo_stock
                guardar_datos(inventario)
                print("stock actualizado correctamente")
            else:
                print("Número fuera de rango")
        except ValueError:
            print("Debes ingresar un número válido")

    elif opcion == "4":
        if len(inventario) == 0:
            print("No hay datos")
        else:
            clave = pedir_texto("Buscar componente:\n")
            encontrados = 0
        for item in inventario:
            if clave.lower() in item["nombre"].lower():
                print(f"- {item["nombre"]} | {item["precio"]:.2f} | {item["stock"]}")
                encontrados += 1
        if encontrados == 0:
            print("No se encontraron coincidencias")
            valor_total = sum(item["precio"] * item["stock"] for item in inventario)
            print(f"Valor total del inventario: ${valor_total:.2f}")

    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no Válida. Elije entre 1 y 5.")
          
              
            
                
                
      
  
      
           































