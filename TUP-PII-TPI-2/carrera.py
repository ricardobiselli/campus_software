class Carrera:
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self._nombre = nombre
        self._cant_anios = cant_anios
        self._cursos = []
        self._alumnos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cant_anios(self):
        return self._cant_anios

    @cant_anios.setter
    def cant_anios(self, cant_anios):
        self._cant_anios = cant_anios

    def __str__(self):
        pass

    def get_cantidad_materias(self) -> int:
        return len(self._cursos)

    @property
    def cursos(self):
        return self._cursos

    def add_curso(self, curso):
        self._cursos.append(curso)

    @property
    def alumnos(self):
        return self._alumnos

    def add_alumno(self, alumno):
        self._alumnos.append(alumno)
