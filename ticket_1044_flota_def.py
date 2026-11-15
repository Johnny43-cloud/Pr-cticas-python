def mostrar_menu():
    print("\n --- SISTEMA DE GESTIÓN DE FLOTA Y MANTENIMIENTO ---")
    print("1. Registrar vehículo y calcular mantenimiento")
    print("2. Ver resumen de flota registrada")
    print("3. Salir del sistema")
  
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("⚠️ El campo no puede estar vacio")
        else:
            return texto
def pedir_numero_positivo(mensaje):
    while True:
        try:
            valor= float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("⚠️ Error: El número debe ser mayor a 0")
        except ValueError:
            print("⚠️ Error ingresé un número válido")
def calcular_mantenimiento(kilometraje):
    if kilometraje >= 50000:
        print(" 🔧 Tipo: Mantenimiento Mayor ($180.0)")
        return  180.0
    elif kilometraje >= 20000:
        print(" 🔧 Tipo: Mantenimiento Intermedio ($95.0)")
        return  95.0
    else:
        print(" 🔧 Tipo: Mantenimiento Básico ($45.0)")
        return  45.0
      
flota = []

while True:
    mostrar_menu()
    opcion = input("Elija una opción (1,2 o 3):\n").strip()
    if opcion == "1":
        placa = pedir_texto("Ingresa la placa del vehículo:\n").upper()
        km = pedir_numero_positivo("Ingresa el kilometraje actual:\n")
        costo = calcular_mantenimiento(km)
     
        vehículo = {"placa": placa, "km": km, "costo": costo}
        flota.append(vehículo)
        print(f"Recibi confirmado| placa:{placa} | km: {km}| Costo a pagar: {costo:.2f}")
    elif opcion == "2":
        if len(flota) == 0:   
            print("📫 Aún no ahí vehículos registrados")
        else:
            print(" --- Resumen de flota registrada ---")
            total_general = 0.0
            for vehículo in flota:
                print(f" Placa: {vehículo['placa']}| km: {vehículo['km']}| costo: {vehículo['costo']:.2f}")
                total_general += vehículo ["costo"]
                print(f" Total acumulado de la flota: {total_general:.2f}")
    elif opcion == "3":
        print(" 👋Saliendo del sistema de flota. ¡Buen trabajo hoy!")
        break
    else:
        print(" ⚠️ Opción inválida: por favor, elije 1,2 o 3")
  
        
