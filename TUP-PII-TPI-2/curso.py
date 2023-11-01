import string
import random
import archivo


class Curso():
    __prox_cod = 10

    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        self.__codigo = Curso.__get_cod_curso()
        self.__archivos = []
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
        
    @property
    def contrasenia_matriculacion(self) -> str:
        return self.__contrasenia_matriculacion
    
    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, contrasenia_matriculacion: str):
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
        
    @property
    def archivos(self) -> list:
        return self.__archivos
    
    def nuevo_archivo(self, archivo: archivo.Archivo):
        self.__archivos.append(archivo)

    @classmethod
    def __get_cod_curso(cls) -> int: # REVISAR QUE QUEDE "CLS" Y NO CLEAR!!!
        cls.__prox_cod += 1
        return cls.__prox_cod

    @classmethod
    def generar_contrasenia(cls): #REVISAR QUE QUEDE "CLS" Y NO CLEAR!!!
        characters = string.ascii_letters + string.digits
        contrasenia = ''.join(random.choice(characters) for _ in range(8))
        return contrasenia
    
    def __str__(self):
        return f"Nombre: {self.__nombre} - Archivos {self.__archivos.nombre}"