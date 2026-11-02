Ejercicio 1: Directorio de contactos

contactos = {
    "Laura": "3001112233",
    "Carlos": "3014445566",
    "Mariana": "3027778899",
    "Andres": "3103334455",
    "Sofia": "3126667788"
}


nombre = input("Nombre a buscar: ")
numero = contactos.get(nombre)
if numero is None:
    print("El contacto no existe.")
else:
    print(f"El número de {nombre} es {numero}")


nombre = input("Nombre a registrar/actualizar: ")
numero = input("Número: ")
if nombre in contactos:
    print("Contacto existente, se actualizará el número.")
else:
    print("Contacto nuevo, se registrará.")
contactos[nombre] = numero


print(f"\n{'NOMBRE':<15}{'TELÉFONO':<12}")
print("-" * 27)
for nombre, numero in contactos.items():
    print(f"{nombre:<15}{numero:<12}")



Ejercicio 2. Frecuencia de palabras


parrafo = "python es rápido y python es legible y practico"


palabras = parrafo.split()

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")



Ejercicio 3. Registro de calificaciones por estudiante

calificaciones = {
    "Carlos": [4.0, 3.5, 4.5],
    "Mariana": [4.8, 5.0, 4.7],
    "Andres": [3.0, 2.8, 3.5]
}

for nombre, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

calificaciones["Carlos"].append(4.0)

mejor_nombre = ""
mejor_promedio = 0
for nombre, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_nombre = nombre

print(f"Mejor promedio: {mejor_nombre} con {mejor_promedio:.2f}")



PROYECTO



catalogo = {
    "P01": {"nombre": "Cuaderno argollado", "precio": 6500, "stock": 20},
    "P02": {"nombre": "Caja de micropuntas", "precio": 18000, "stock": 12},
    "P03": {"nombre": "Resma de papel", "precio": 15000, "stock": 8}
}


def buscar_producto():
    codigo = input("Código del producto: ").upper()
    producto = catalogo.get(codigo)
    if producto is None:
        print("Advertencia: el código no existe en el catálogo.")
    else:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")


def ingresar_existencias():
    codigo = input("Código del producto: ").upper()
    if codigo not in catalogo:
        print("Advertencia: el código no existe en el catálogo.")
        return
    cantidad = input("Cantidad a ingresar: ")
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Cantidad inválida.")
        return
    catalogo[codigo]["stock"] += int(cantidad)
    print(f"Nuevo stock: {catalogo[codigo]['stock']}")


def registrar_producto():
    codigo = input("Código nuevo: ").upper()
    if codigo in catalogo:
        print(f"El código ya existe ({catalogo[codigo]['nombre']}).")
        confirmar = input("¿Desea sobreescribirlo? (s/n): ").lower()
        if confirmar != "s":
            print("Operación cancelada.")
            return
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    stock = input("Stock: ")
    if not precio.isdigit() or not stock.isdigit():
        print("Precio y stock deben ser números enteros.")
        return
    catalogo[codigo] = {"nombre": nombre, "precio": int(precio), "stock": int(stock)}
    print("Producto guardado.")


def valor_inventario():
    total = 0
    for codigo, datos in catalogo.items():
        total += datos["precio"] * datos["stock"]
    print(f"Valor total del inventario: ${total}")


def menu():
    while True:
        print("\n--- CATÁLOGO DE LA TIENDA ---")
        print("1. Buscar producto")
        print("2. Ingresar existencias")
        print("3. Registrar producto nuevo")
        print("4. Valor total del inventario")
        print("5. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            buscar_producto()
        elif opcion == "2":
            ingresar_existencias()
        elif opcion == "3":
            registrar_producto()
        elif opcion == "4":
            valor_inventario()
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


menu()
