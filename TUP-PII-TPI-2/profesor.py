from usuario import Usuario
from curso import listado_cursos
import datos

class Profesor(Usuario):
    def __init__(self, titulo: str, anio_egreso: int, nombre: str, apellido: str, email: str, password:str): 
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        super().__init__(nombre, apellido, email, password)

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def anio_egreso(self):
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, value):
        self.__anio_egreso = value

    def __str__(self):
        return f"{self.nombre.title()} {self.apellido.title()}"

    def dictar_curso(self, objeto_activo, nuevo_objeto_curso, carrera):
        objeto_activo._mis_cursos.append(nuevo_objeto_curso) # agregar curso a la lista de cursos del profesor
        listado_cursos.append(nuevo_objeto_curso) # agregar curso a la lista general de cursos
        carrera._cursos.append(nuevo_objeto_curso) # agregar curso a la carrera