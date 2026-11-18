import json
try:
    with open("/tmp/inventario_pc.json","r",encoding="utf-8") as archivo:
        productos = json.load(archivo)
except (FileNotFoundError, json.JSONDecodeError):
    productos = []
  
def mostrar_menu():
    print("1. Registrar nuevo producto")
    print("2. Ver inventario y valor total")
    print("3. Buscar producto por nombre")
    print("4. Salir")
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("⚠️ El campo no puede estar vacío")
        else:
            return texto
def pedir_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("⚠️ Error: El número debe ser mayor a 0")
        except ValueError:
            print("⚠️ Error ingresé un precio válido (ej.12.50")
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("⚠️Error: La cantidad debe ser mayor a 0")
        except ValueError:
            print("⚠️ Error: ingresa una cantidad entera válida (sin decimales)")
while True:
    mostrar_menu()
    opcion = input("Elija una opcion (1,2,3 o 4):\n").strip()
    if opcion == "1":
        nombre = pedir_texto("Ingresa el nombre del nuevo producto:\n")
        precio = pedir_precio("Ingrese el precio del producto:\n")
        stock = pedir_entero("Ingrese la cantidad en stock:\n")
        producto = {"nombre": nombre,"precio": precio,"stock": stock}
        productos.append(producto)
        print(f"productos|nombre: {nombre}|precio:{precio}|stock:{stock} guardados correctamente")
        with open("/tmp/inventario_pc.json","w",encoding="utf-8") as archivo:
            json.dump(productos,archivo,indent=4,ensure_ascii = False)
    elif opcion == "2":
        if len(productos) == 0:
            print("Aún no ahí productos agregados")
        else:
            print("\n--- RESUMEN DE INVENTARIO Y VALOR TOTAL ---")
            total_general = 0.0
        for producto in productos:
            subtotal = producto['precio'] * producto['stock']
            print(f"nombre: {producto['nombre']}| precio:{producto['precio']:.2f}| stock: ${producto['stock']}| subtotal: ${subtotal:.2f}")
            total_general += subtotal
        print(f"Valor total del inventario: {total_general:.2f}")
    elif opcion == "3":
        busqueda = pedir_texto("Ingresa el nombre del producto a buscar:\n").lower()
        encontrado = False
        for producto in productos:
            if busqueda in producto["nombre"].lower():
                print(f"Encontrado: {producto['nombre']}| precio: ${producto['precio']:.2f}| stock: {producto['stock']}")
                encontrado = True
        if not encontrado:
            print("No se encontró ningún producto con ese nombre")
    elif opcion == "4":
        print("¡Hasta luego! Inventario guardado en /tmp/inventario_pc.json ")
        break
    else:
        print("⚠️ Opcion no válida. Elije 1,2,3 o 4")
       
            
      
            
        
      
        
          
      
          

