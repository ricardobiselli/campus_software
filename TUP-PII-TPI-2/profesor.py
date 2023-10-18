from usuario import Usuario

class Profesor(Usuario):
    
    def __init__(self, titulo: str, anio_egreso: int, nombre: str, apellido: str, email: str, password:str): 
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        super().__init__(nombre, apellido, email, password)

    def __str__(self):
        pass

    """def dictar_curso(curso):  # curso:Curso
        pass"""
