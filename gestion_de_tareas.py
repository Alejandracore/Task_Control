class Tarea:
    def __init__(self, id, titulo, descripcion= ""):
     self.id = id
     self.titulo = titulo
     self. descripcion = descripcion
     self.completada = False 

    tarea = []
    siguiente_id = 1 

    def registar_tarea(titulo, descripcion=""):
       global siguiente_id
       if not titulo.strip():
        return False
       tarea = Tarea(siguiente_id, titulo, descripcion)
       tarea.append(tarea)
       siguiente_id += 1
       return True