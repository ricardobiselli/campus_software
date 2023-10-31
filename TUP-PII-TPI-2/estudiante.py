from usuario import *


class Estudiante(Usuario):
    def __init__(
        self,
        legajo: int,
        anio_inscripcion_carrera: int,
        nombre: str,
        apellido: str,
        email: str,
        contrasenia: str,
    ):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    @property
    def legajo(self):
        return self.__legajo

    @legajo.setter
    def legajo(self, legajo):
        self.__legajo = legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera

    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, anio_inscripcion_carrera):
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    @property
    def mis_cursos(self):
        return self._mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, cursos):
        self._mis_cursos = cursos

    def __str__(self):
        return f"{self.nombre.title()} {self.apellido.title()}"

    def matricular_en_curso(self, objeto_activo, curso_a_matricularse):
        objeto_activo._mis_cursos.append(curso_a_matricularse)

    def desmatricular_curso(self, objeto_activo, curso_a_desmatricularse):
        objeto_activo._mis_cursos.remove(curso_a_desmatricularse)
