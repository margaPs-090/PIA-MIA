agenda = {"ana":655897123, "leo": 986547390, "eva": 657894123 }

while True:
    print("\n1. Alta")
    print("2. Baja")
    print("3. Buscar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono

    elif opcion == "2":
        nombre = input("Nombre a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado")
        else:
            print("No existe")

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        if nombre in agenda:
            print(agenda[nombre])
        else:
            print("No encontrado")

    elif opcion == "4":
        for nombre in sorted(agenda):
            print(nombre, "-", agenda[nombre])

    elif opcion == "5":
        break