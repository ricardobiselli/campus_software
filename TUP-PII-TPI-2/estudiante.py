from usuario import *


class Estudiante(Usuario):
    def __init__(self, legajo: int, anio_inscripcion_carrera: int, nombre: str, apellido: str, email: str, password:str):
        super().__init__(nombre, apellido, email, password)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
    
    @property
    def mis_cursos(self):
        return self._mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, cursos):
        self._mis_cursos = cursos


    def matricular_en_curso(self, objeto_activo, curso_a_matricularse):
        objeto_activo._mis_cursos.append(curso_a_matricularse)