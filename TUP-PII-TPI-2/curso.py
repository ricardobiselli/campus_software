import string
import random
import archivo


class Curso():
    _prox_cod = 10

    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self._nombre = nombre
        self._contrasenia_matriculacion = contrasenia_matriculacion
        self._codigo = Curso._get_cod_curso()
        self._archivos = []
    
    def nuevo_archivo(self, archivo: archivo.Archivo):
        self._archivos.append(archivo)

    @classmethod
    def _get_cod_curso(cls) -> int:
        cls._prox_cod += 1
        return cls._prox_cod

    
    @classmethod
    def generar_contrasenia(cls):
        characters = string.ascii_letters + string.digits
        contrasenia = ''.join(random.choice(characters) for _ in range(8))
        return contrasenia
    
    def __str__(self):
        return f"Nombre: {self._nombre} - Archivos {self._archivos.nombre}"


#mover todo a datos
curso_1 = Curso("programación 1", "prog1")
curso_2 = Curso("programación 2", "prog2")
curso_3 = Curso("inglés 1", "ing1")
curso_4 = Curso("inglés 2", "ing2")
curso_5 = Curso("laboratorio 1", "lab1")
curso_6 = Curso("laboratorio 2", "lab2")

listado_cursos = [curso_1, curso_2, curso_3, curso_4, curso_5, curso_6]

#listado_cursos = []
