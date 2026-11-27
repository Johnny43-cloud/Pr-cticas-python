import json
ARCHIVO = "/tmp/inventario_crud.json"

def cargar_datos():
    try:
        with open(ARCHIVO,"r",encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return []
        return []
      
def guardar_datos(inventario):
    with open(ARCHIVO,"w",encoding="utf-8") as f:
        json.dump(inventario, f, indent=4 ,ensure_ascii=False)
                  
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("El campo no puede estar vacío ")
        else:
            return texto
          
def pedir_float_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El monto debe ser mayor a 0")
        except ValueError:
            print("⚠️ Error: Ingrese una cantidad válida")
          
def pedir_entero_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("El stock no puede ser negativo (0 o más)")
        except ValueError:
            print("⚠️ Error: Ingrese un entero válido")

inventario = cargar_datos()

while True:
    print("\n1. Agregar producto")
    print("2. Ver inventario y valor total")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Elige una opcion (1-5):\n")

    if opcion == "1":
        nombre = pedir_texto("Ingrese el nombre del producto:\n")
        precio = pedir_float_positivo("Ingrese el precio del producto:\n")
        stock = pedir_entero_no_negativo("Ingrese la cantidad en stock:\n")
        item = {"nombre":nombre, "precio": precio, "stock":stock ,"completado":False}
        inventario.append(item)
        guardar_datos(inventario)
        print("Datos guardados exitosamente")

    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay datos registrados")
        else:
            print(" --- LISTA DEL INVENTARIO ---")
        for i, item in enumerate(inventario,start=1):
            if item["stock"] == 0:
                estado = "[AGOTADO]"
            else:
                estado = "[DISPONIBLE]"
                print(f"{i}.{estado} {item['nombre']} | {item['precio']:.2f} | stock: {item['stock']}")
        valor_total = sum(p["precio"] * p["stock"] for p in inventario)
        print(f"Valor total del inventario: {valor_total:.2f}")

    elif opcion == "3":
        if len(inventario) == 0:
            print("No hay datos registrados")
        else:
            for i, item in enumerate(inventario,start=1):
                if item["stock"] == 0:
                    estado = "[AGOTADO]"
                else:
                    estado = "[DISPONIBLE]"
                    print(f"{i}.{estado} {item['nombre']} | {item['precio']:.2f} | stock: {item['stock']}")
            try:
                num = int(input("Numero del producto a actualizar:\n"))
                if 1 <= num <= len(inventario):
                    nuevo_stock = pedir_entero_no_negativo("Nuevo stock:\n")
                    inventario[num - 1]["stock"] = nuevo_stock
                    guardar_datos(inventario)
                    print("Stock actualizado correctamente")
                else:
                    print("Numero fuera de rango")
            except ValueError:
                print("Debes ingresar un número válido")

    elif opcion == "4":
        if len(inventario) == 0:
            print("No hay datos registrados")
        else:
            for i, item in enumerate(inventario,start=1):
                if item["stock"] == 0:
                    estado = "[AGOTADO]"
                else:
                    estado = "[DISPONIBLE]"
                    print(f"{i}.{estado} {item['nombre']} | {item['precio']:.2f} | stock: {item['stock']}")
            try:
                num = int(input("Numero del producto a eliminar:\n"))
                if 1 <= num <= len(inventario):
                    eliminado = inventario.pop(num - 1)
                    guardar_datos(inventario)
                    print(f"Producto eliminado: {eliminado['nombre']} eliminado correctamente")
                else:
                    print("Numero fuera de rango")
            except ValueError:
                print("Debes ingresar un número válido")

    elif opcion == "5":
        print("Saliendo del sistema.¡Hasta luego!.")
        break
    else:
        print("Opcion inválida. Elige entre 1 y 5.")
         
          


































































