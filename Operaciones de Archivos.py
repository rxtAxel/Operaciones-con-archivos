archivo = "registros.txt"

while True:
    print("\n1. Crear archivo")
    print("2. Guardar registros")
    print("3. Leer archivo")
    print("4. Actualizar nombre")
    print("5. Cerrar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        f = open(archivo, "w")
        f.close()
        print("Archivo creado.")

    elif opcion == "2":
        nombre = input("Nombre: ")
        matricula = input("Matrícula: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")

        f = open(archivo, "a")
        print("NOMBRE:", nombre, file=f)
        print("MATRICULA:", matricula, file=f)
        print("CORREO:", correo, file=f)
        print("TELEFONO:", telefono, file=f)
        print("", file=f)
        f.close()
        print("Registro guardado.")

    elif opcion == "3":
        try:
            f = open(archivo, "r")
            print(f.read())
            f.close()
        except:
            print("El archivo no existe.")

    elif opcion == "4":
        nombre_buscar = input("Nombre a buscar: ")
        nuevo_nombre = input("Nuevo nombre: ")

        try:
            f = open(archivo, "r")
            lineas = f.readlines()
            f.close()

            f = open(archivo, "w")
            for linea in lineas:
                if linea.startswith("NOMBRE:") and nombre_buscar in linea:
                    print("NOMBRE:", nuevo_nombre, file=f)
                else:
                    print(linea.strip(), file=f)
            f.close()
            print("Nombre actualizado.")
        except:
            print("El archivo no existe.")

    elif opcion == "5":
        print("Programa cerrado.")
        break

    else:
        print("Opción inválida.")
