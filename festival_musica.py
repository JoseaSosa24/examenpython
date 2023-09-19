# Menú de opciones
# Registrar agrupación musical: id, nombre, genero, hora en la que se presenta, pago que se le da a la agrupación, estado (true si ya se presentó/ false si aún no han tocado)
# Buscar y mostrar en consola todas las bandas que no se han presentado
# Cambiar la hora de presentación de una agrupación que no se haya presentado aún
# Retirar una agrupación que no se ha presentado del listado de agrupaciones

opcion = 0

print("*********************")
print("\nMenú de opciones:")
print("1. Registrar una agrupación musical")
print("2. Mostrar todas las agrupaciones que no se han presentado")
print("3. Cambiar la hora de presentación de una agrupación")
print("4. Retirar una agrupación que no se ha presentado")
print("5. Salir")
print("\n*********************")
agrupaciones = [
    {
        "id": 1,
        "nombre": "Banda A",
        "genero": "Rock",
        "hora": "19:00",
        "pago": 1500.0,
        "estado": False
    },
    {
        "id": 2,
        "nombre": "Grupo B",
        "genero": "Pop",
        "hora": "20:30",
        "pago": 1200.0,
        "estado": False
    },
    {
        "id": 3,
        "nombre": "Orquesta C",
        "genero": "Clásica",
        "hora": "18:15",
        "pago": 2000.0,
        "estado": False
    },
    {
        "id": 4,
        "nombre": "Dúo D",
        "genero": "Folk",
        "hora": "21:45",
        "pago": 900.0,
        "estado": False
    },
    {
        "id": 5,
        "nombre": "Banda E",
        "genero": "Indie",
        "hora": "22:00",
        "pago": 1800.0,
        "estado": False
    }
]

while opcion != 5:
    agrupacion = {}
    opcion = int(input("\nDigita la opción deseada: "))

    # Registrando agrupación musical
    if opcion == 1:
        agrupacion["id"] = int(input("\nDigita el id de la agrupación: "))
        agrupacion["nombre"] = input("Digita el nombre de la agrupación: ")
        agrupacion["genero"] = input("Digita el genero musical: ")
        agrupacion["hora"] = input("Digita la hora de presentación: ")
        agrupacion["pago"] = float(input("Digita el pago a la agrupación: "))
        agrupacion["estado"] = False
        agrupaciones.append(agrupacion)
        print("\nAgrupación registrada con éxito.")

    elif opcion == 2:
        # Mostrando todas las agrupaciones que no se han presentado
        print("Agrupaciones que aún no se han presentado:")
        for agrupacion in agrupaciones:
            if not agrupacion["estado"]:
                print (f"Id: {agrupacion ['id']}")
                print (f"Nombre: {agrupacion ['nombre']}")
                print (f"Género: {agrupacion ['genero']}")
                print (f"Hora: {agrupacion ['hora']}")
                print (f"Pago: {agrupacion ['pago']}")
                print (f"Estado: {agrupacion ['estado']}")
                print("\n*********************")
    elif opcion == 3:
        # Cambiando la hora de presentación de una agrupación que no se ha presentado aún
        id_buscar = int(input("\nIngrese el ID de la agrupación cuya hora de presentación desea cambiar: "))
        for agrupacion in agrupaciones:
            if agrupacion["id"] == id_buscar and not agrupacion["estado"]:
                nueva_hora = input("Ingrese la nueva hora de presentación: ")
                agrupacion["hora"] = nueva_hora
                print("Hora de presentación actualizada con éxito.")
                break
        else:
            print("\nAgrupación no encontrada o ya se ha presentado.")
            
    elif opcion == 4:
        # Retirando una agrupación que no se ha presentado del listado de agrupaciones
        id_retirar = int(input("\nIngrese el ID de la agrupación que desea retirar: "))
        for agrupacion in agrupaciones:
            if agrupacion["id"] == id_retirar and not agrupacion["estado"]:
                agrupaciones.remove(agrupacion)
                print("Agrupación retirada con éxito.")
                break
        else:
            print("\nAgrupación no encontrada o ya se ha presentado.")

    elif opcion == 5:
        # Salir del programa
        print("¡Excelente festival, nos vemos en 2024!")
        break

    else:
        print("\nOpción no válida. Por favor, seleccione una opción válida.")