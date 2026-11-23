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