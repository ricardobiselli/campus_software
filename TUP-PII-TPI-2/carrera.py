class Carrera():
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self._nombre =  nombre
        self._cant_anios = cant_anios
    
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
    
    def get_cantidad_materias()->int:
        pass