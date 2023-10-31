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
    def _get_cod_curso(cls) -> int: # REVISAR QUE QUEDE "CLS" Y NO CLEAR!!!
        cls._prox_cod += 1
        return cls._prox_cod

    @classmethod
    def generar_contrasenia(cls): #REVISAR QUE QUEDE "CLS" Y NO CLEAR!!!
        characters = string.ascii_letters + string.digits
        contrasenia = ''.join(random.choice(characters) for _ in range(8))
        return contrasenia
    
    def __str__(self):
        return f"Nombre: {self._nombre} - Archivos {self._archivos.nombre}"