class Carrera:
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__cursos = []
        self.__alumnos = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def cant_anios(self):
        return self.__cant_anios

    @cant_anios.setter
    def cant_anios(self, cant_anios):
        self.__cant_anios = cant_anios

    def __str__(self):
        pass

    def get_cantidad_materias(self) -> int:
        return len(self._cursos)

    @property
    def cursos(self):
        return self.__cursos

    def add_curso(self, curso):
        self.__cursos.append(curso)

    @property
    def alumnos(self):
        return self.__alumnos

    def add_alumno(self, alumno):
        self.__alumnos.append(alumno)
