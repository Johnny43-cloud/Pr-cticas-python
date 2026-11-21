import json
try:
    with open("/tmp/finanzas_v2.json","r",encoding="utf-8") as archivo:
        movimientos = json.load(archivo)
except (FileNotFoundError, json.JSONDecodeError):
    movimientos = []
  
def guardar_movimientos(movimientos):
    with open("/tmp/finanzas.json","w",encoding="utf-8") as archivo:
        json.dump(movimientos, archivo, indent=4, ensure_ascii=False)
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("⚠️ Error: El campo no puede estar vacío ")
        else:
            return texto
          
def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("⚠️ Error: El monto debe ser mayor a 0")
            else:
                return valor 
        except ValueError:
            print("⚠️ Error: Ingrese una cantidad válida")

def mostrar_movimientos(movimientos):
    if len(movimientos) == 0:
        print(" No hay movimientos registrados")
        return False
    else:
        print("\n --- LISTAS DE MOVIMIENTOS---")
        for i, m in enumerate(movimientos, start=1):
                print(f" {i}. [{m['tipo'].upper()}], {m['concepto']} | ${m['monto']:.2f}")
        return True
def mostrar_menu():
    print("\n--- CONTROL DE FINANZAS ---")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver historial de movimiento")
    print("4. Ver resumen financiero")
    print("5. Salir")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion (1-5):\n").strip()
  
    if opcion == "1":
        concepto = pedir_texto("Ingrese el concepto del ingreso:\n")
        monto = pedir_float("Ingrese el monto ($):\n")
        movimiento = {"tipo":"ingreso", "concepto": concepto, "monto":monto}
        movimientos.append(movimiento)
        guardar_movimientos(movimientos)
        print("Ingreso registrado exitosamente")
      
    elif opcion == "2":
        concepto = pedir_texto("Ingrese el concepto del gasto:\n")
        monto = pedir_float("Ingrese el monto ($):\n")
        movimiento = {"tipo":"gasto", "concepto": concepto, "monto":monto}
        movimientos.append(movimiento)
        guardar_movimientos(movimientos)
        print("Gasto registrado exitosamente")
      
    elif opcion == "3":
        mostrar_movimientos(movimientos)
    elif opcion == "4":
        total_ingresos = sum(m['monto'] for m in movimientos if m['tipo'] == "ingreso")
        total_gastos = sum(m['monto'] for m in movimientos if m['tipo'] == "gasto")
        balance = total_ingresos - total_gastos
        print(f" Total ingresos: ${total_ingresos:.2f}")
        print(f" Total gastos:   ${total_gastos:.2f}")
        print(f" Balance neto:   ${balance:.2f}")
    elif opcion == "5":
        print("¡Hasta luego! Saliendo del control de finanzas")
        break
    else:
        print("⚠️ Opción no Válida. por favor, elije 1,2,3,4 o 5")
        































  
  
          
  
        
