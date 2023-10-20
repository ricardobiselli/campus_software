import string
import random

class Curso():
    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self.nombre = nombre
        self.contrasenia_matriculacion = contrasenia_matriculacion
   
def generar_contrasenia():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod    

