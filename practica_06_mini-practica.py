while True:
    nombre = input("Escribe tu nombre (solo letras):\n").strip()
    if nombre.isalpha():
        print(f"✅ Hola, {nombre}")
        break
    else:
        print("⚠️ Error: No se permiten números ni símbolos. Escribe solo letras.")
      
