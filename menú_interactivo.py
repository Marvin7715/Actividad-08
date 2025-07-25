productos = []

while True:
    print("\n=== MENÚ INTERACTIVO ===")
    print("1. Agregar un producto a la lista")
    print("2. Modificar un producto existente")
    print("3. Eliminar un producto")
    print("4. Ver todos los productos")
    print("5. Salir del programa")

    opcion = input("Seleccione una opción (1-5): ")

    match opcion:
        case "1":
            nuevo = input("Ingrese un nuevo producto a la lista: ")
            productos.append(nuevo)
            print("Producto agregado.")

        case "2":
            print("Lista actual:", productos)
            indice = int(input("Ingrese el índice del producto a modificar: "))
            nuevo_valor = input("Ingrese el nuevo elemento: ")
            productos[indice] = nuevo_valor
            print("Producto modificado.")

        case "3":
            print("Lista actual:", productos)
            valor = input("Ingrese el valor a eliminar: ")
            productos.remove(valor)
            print("Elemento eliminado.")

        case "4":
            print("Lista actual:", productos)

        case "5":
            print("¡Saliendo del menú!")
            break

        case _:
            print("Opción no válida. Repitalo de nuevo")