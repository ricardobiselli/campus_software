from usuario import *

class Estudiante(Usuario):
    def __init__(self, legajo: int, anio_inscripcion_carrera: int, nombre: str, apellido: str, email: str, password:str):
        super().__init__(nombre, apellido, email, password)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera


    #def matricular_en_curso(): 
        pass