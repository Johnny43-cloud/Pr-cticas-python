# ARCHIVO: checkout_clientes.py
# ESTADO: ARREGLADO EN PRODUCCIÓN

print("=== SISTEMA DE PEDIDOS ===")

while True:
    nombre = input("Nombre del cliente:\n").strip()
    if nombre.isalpha():
        break
    else:
        print("⚠️Error: Ingrese un nombre válido, (solo letras)")
while True:
    try:
        precio = float(input("Precio unitario del producto ($):\n"))
        if precio <= 0:
            print("⚠️Error: El precio debe ser mayor a 0")
        else:
            break
    except ValueError:
            print("⚠️Error: Ingrese un numero válido para el precio")
while True:
    try:
        cantidad = int(input("Cantidad de unidades:\n"))
        if cantidad <=0:
             print("⚠️Error: La cantidad no debe ser mayor a 0")
        else:
            break
    except ValueError:
            print("⚠️Error: Ingrese la cantidad valida para las unidades ")
total = precio * cantidad

print(f"\n✅ Pedido confirmado para {nombre}")
print(f"Total a pagar: ${round(total, 2)}")
