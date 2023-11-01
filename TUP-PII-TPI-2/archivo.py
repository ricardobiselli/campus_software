from datetime import date

class Archivo():
    def __init__(self, nombre: str, formato: str) -> None:
        self.__nombre = nombre
        self.__fecha = date.today()
        self.__formato = formato
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
        
    @property
    def formato(self):
        return self.__formato
    
    @formato.setter
    def formato(self, formato):
        self.__formato = formato
        
    def __str__(self) -> str:
        return f"{self.nombre} - ({self.formato}) - fecha: {self.fecha}"
    