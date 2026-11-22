contactos = [
    {"nombre": "Ana", "telefono": "0991112222"},
    {"nombre": "Carlos", "telefono": "0983334444"},
    {"nombre": "María", "telefono": "0975556666"}
]
while True:
    print("\n1. Ver contactos\n2. Buscar contacto\n3.Salir ")
    opcion = input("Elije una opcion (1-3):\n")
    if opcion == "1":
        for c in contactos:
            print(f"{c['nombre']} - {c['telefono']}")
    elif opcion == "2":
        buscar = input("Nombre a buscar:\n").strip().lower()
        encontrado = False
        for c in contactos:
            if buscar in c["nombre"].lower():
                print(f"{["nombre"]} - {c["telefono"]}")
                encontrado = True
            if not encontrado:
                print(" contacto no encontrado ")
    else:
        break
