class Tarea:
    def __init__(self, id, titulo, descripcion= ""):
    self.id = id
    self.titulo = titulo
    self.descripcion = descripcion
    self.completada = False 

    tareas = []
    siguiente_id = 1 