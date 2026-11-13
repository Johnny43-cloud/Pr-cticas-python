# ARCHIVO: caja_registradora_bug.py
# ESTADO: RESUELTO - TICKET #1043

precios = {
    "Pan": 0.50,
    "Leche": 1.25,
    "Cafe": 3.00,
    "Queso": 2.75
}

print("=== CAJA REGISTRADORA ===")
while True:
          producto = input("¿Qué producto lleva el cliente?:\n").strip().capitalize()
          if producto in precios:
              print(f" ✔️ Listo: {producto} econtrado")
              break
          else:
              print(f" ⚠️ Error: {producto} no encontrado")
while True:
    try:
        cantidad = int(input("¿Cuántas unidades lleva?:\n"))
        if cantidad <= 0:
              print("⚠️ Error: la cantidad debe ser mayor a 0")
        else:
              break
    except ValueError:
              print("⚠️ Error: Ingrese un número válido")
total = precios[producto] * cantidad

print(f"\n✅ Cobro exitoso: {cantidad}x {producto}")
print(f"Total a cobrar: ${total:.2f}")
