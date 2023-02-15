class Materia ():
    def __init__ (self, nombre, horas_por_semana, requirements=[]):
        self.nombre = nombre
        self.horas_por_semana = horas_por_semana
        self.requirements = requirements # materias necesarias para cursar

    def __str__ (self):
        return self.nombre

class Cuatrimestre ():
    def __init__ (self, materias, year, n_cuatrim):
        self.materias = materias
        self.year = year
        self.n_cuatr = n_cuatrim
    
    def get_date_info(self):
        return self.year, self.n_cuatr

class PlanDeEstudios ():
    def __init__ (self, titulo:str, tipo:str,
                  json_data:dict, reward:int):
        self.materias = []
        for cuatrim in json_data:
            self.materias += json_data[cuatrim] 
        self.tipo = tipo
        self.titulo = titulo
        self.reward = reward