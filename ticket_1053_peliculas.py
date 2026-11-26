peliculas = []

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print(" El campo no puede estar vacío ")
        else:
            return texto
while True:
    print("\n1. Agregar película")
    print("2. Ver todas las películas")
    print("3. Marcar película como vista")
    print("4. Salir")
    opcion = input("Elige una opcion (1-4):\n").strip()
  
    if opcion == "1":
        titulo = pedir_texto("Ingrese el nombre de la película:\n")
        genero = pedir_texto("Ingrese el genero de la película:\n")
        item = {"titulo": titulo, "genero":genero, "vista":False}
        peliculas.append(item)
        print("registrado exitosamente")

    elif opcion == "2":
        if len(peliculas) == 0:
            print("No hay registradas")
        else:
            print("\n --- LISTA DE PELÍCULAS ---")
        for i, item in enumerate(peliculas,start=1):
            if item["vista"]:
                estado = "[x]"
            else:
                estado = "[ ]"
                print(f"{i}. {estado} {item['titulo']} | {item['genero']}")

    elif opcion == "3":
        if len(peliculas) == 0:
            print("No hay registradas")
        else:
            for i, item in enumerate(peliculas,start=1):
                if item["vista"]:
                    estado = "[x]"
                else:
                    estado = "[ ]"
                    print(f"{i}. {estado} {item['titulo']} | {item['genero']}")
            try:
                num = int(input("Numero de película a ver:\n"))
                if 1 <= num <= len(peliculas):
                    peliculas[num - 1]["vista"]=True
                    print("pelicula registrada exitosamente")
                else:
                    print("Numero fuera de rango")
            except ValueError:
                print("Debes ingresar un número válido")

    elif opcion == "4":
        print("Saliendo del sistema. ¡Hasta luego!.")
        break
          
          

      
