import json

ARCHIVO = "/tmp/gastos.json"

def cargar_datos():
    try:
        with open(ARCHIVO,"r",encoding="utf-8") as f:
            datos = json.load(f)
            return datos if isinstance (datos, list) else[]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(gastos):
    with open(ARCHIVO,"w",encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("El campo no puede estar vacío")
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
            print("⚠️Error: Ingrese una cantidad válida")

gastos = cargar_datos()

while True:
    print("\n1. Registrar gastos")
    print("2. Ver historial")
    print("3. Ver total gastado")
    print("4. Salir")
    opcion = input("Elige una opcion (1-4):\n").strip()

    if opcion == "1":
        categoria = pedir_texto("categoria. (ej: comida, transporte , ocio):\n")
        monto = pedir_float_positivo("Monto del gasto ($):\n")
        item = {"categoria":categoria, "monto":monto}
        gastos.append(item)
        guardar_datos(gastos)
        print(f"gastos | categoria: {categoria} | monto: {monto} guardados correctamente")

    elif opcion == "2":
        if len(gastos) == 0:
            print("No hay gastos registrados ")
        else:
            print("\n --- HISTORIAL DE GASTOS ")
            for i, item in enumerate(gastos, start=1):
                print(f" {i}. {item["categoria"]} | {item["monto"]:.2f}")

    elif opcion == "3":
        if len(gastos) == 0:
            print("Total gastado: $0.0 ")
        else:
            total = sum(g["monto"] for g in gastos)
            print(f"Total gastado: ${total:.2f}")

    elif opcion == "4":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Elige entre 1 y 4.")
        
          













































      
            
