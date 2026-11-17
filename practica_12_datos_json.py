import json
#tareas =[{"Titulo": "Aprender JSON","estado":"completado"},{"Titulo":"Subir codigo a GItHub","estado":"pendiente"}]

#with open("/tmp/tareas.json","w",encoding="utf-8") as archivo:
    #json.dump(tareas, archivo, indent=4,ensure_ascii = False)
#try:
    #with open("/tmp/tareas.json","r",encoding="utf-8") as archivo:
      #tareas_cargadas = json.load(archivo)
#except FileNotFoundError:
   #(tareas_cargadas) == []
#print(tareas_cargadas)
try:
    with open("/tmp/metas.json","r",encoding="utf-8") as archivo:
        metas = json.load(archivo)
except (FileNotFoundError, json.JSONDecodeError):
    metas = []

def mostrar_menu():
    print("1. Agregar nueva meta")
    print("2. Ver todas mis metas")
    print("3. Salir")
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto =="":
            print("⚠️ El campo no puede estar vacío")
        else:
            return texto
while True:
    mostrar_menu()
    opcion = input("Elija una opcion (1,2 o 3):\n").strip()
    if opcion == "1":
        titulo = pedir_texto("Ingresa el titulo de tu meta:\n")
        categoria = pedir_texto("Ingresa la categoria (ej. programación , inglés):\n")
        meta = {"titulo": titulo,"categoria": categoria}
        metas.append(meta)
        print(f"meta,{titulo} guardada correctamente")
        with open("/tmp/metas.json","w",encoding="utf-8") as archivo:
            json.dump(metas,archivo,indent=4,ensure_ascii = False)
    elif opcion == "2":
        if len(metas) == 0:
            print("📪 No tienes metas guardadas")
        else:
            print("📪 Total de metas registradas")
            for i, m in enumerate(metas,start=1):
                print(f"{i}. [{m['categoria']}] {m['titulo']}")
    elif opcion == "3":
        print("👋¡Hasta luego! tus metas quedaron guardadas")
        break
    else:
        print("⚠️ Opción inválida: por favor elije 1,2 o 3")
            
  
    









      
