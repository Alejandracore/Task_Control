class Tarea:
    def __init__(self, id, titulo, descripcion=""):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False


tareas = []
siguiente_id = 1


def registrar_tarea(titulo, descripcion=""):
    global siguiente_id

    if not titulo.strip():
        return False

    nueva_tarea = Tarea(siguiente_id, titulo, descripcion)
    tareas.append(nueva_tarea)
    siguiente_id += 1

    return True


def buscar_tarea(id_tarea):
    for tarea in tareas:
        if tarea.id == id_tarea:
            return tarea

    return None


def cambiar_estado(id_tarea, estado):
    tarea = buscar_tarea(id_tarea)

    if tarea is None:
        return False

    tarea.completada = estado
    return True


def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    for tarea in tareas:
        estado = "Completada" if tarea.completada else "Pendiente"

        print(f"ID: {tarea.id}")
        print(f"Titulo: {tarea.titulo}")
        print(f"Descripcion: {tarea.descripcion}")
        print(f"Estado: {estado}")
        print("----------------------")


def elimina_tarea(id_tarea):
    tarea = buscar_tarea(id_tarea)

    if tarea is None:
        return False

    tareas.remove(tarea)
    return True


def filtar_tareas(estado):
    return [tarea for tarea in tareas if tarea.completada == estado]


def menu():
    while True:
        print("\n -------- Task Control --------")
        print("1. Registrar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Reabrir tarea")
        print("5. Eliminar tarea")
        print("6. Filtrar tareas")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            descripcion = input("Descripcion: ")

            if registrar_tarea(titulo, descripcion):
                print("Tarea registrada correctamente.")
            else:
                print("El titulo no puede estar vacio.")

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            id_tarea = int(input("ID de la tarea: "))
            print(
                "Tarea completada."
                if cambiar_estado(id_tarea, True)
                else "Tarea no encontrada."
            )

        elif opcion == "4":
            id_tarea = int(input("ID de la tarea: "))
            print(
                "Tarea reabierta."
                if cambiar_estado(id_tarea, False)
                else "Tarea no encontrada."
            )

        elif opcion == "5":
            id_tarea = int(input("ID de la tarea: "))
            print(
                "Tarea eliminada correctamente."
                if elimina_tarea(id_tarea)
                else "Tarea no encontrada."
            )

        elif opcion == "6":
            estado = input("Filtrar por (1. Completadas / 2. Pendientes): ")

            if estado == "1":
                resultado = filtar_tareas(True)
            elif estado == "2":
                resultado = filtar_tareas(False)
            else:
                print("Opcion no valida.")
                continue

            if not resultado:
                print("No hay tareas con ese estado.")
            else:
                for tarea in resultado:
                    estado_tarea = "Completada" if tarea.completada else "Pendiente"
                    print(f"ID: {tarea.id}")
                    print(f"Titulo: {tarea.titulo}")
                    print(f"Descripcion: {tarea.descripcion}")
                    print(f"Estado: {estado_tarea}")
                    print("----------------------")

        elif opcion == "7":
            print("Gracias por utilizar Task Control.")
            break

        else:
            print("Opcion no valida.")


menu()