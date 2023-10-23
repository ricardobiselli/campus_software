import string
import random

class Curso():
    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self.nombre = nombre
        self.contrasenia_matriculacion = contrasenia_matriculacion

def __generar_contrasenia():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod

#falta agregar carrera!!!
curso_1 = Curso("programación 1", "prog1")
curso_2 = Curso("programación 2", "prog2")
curso_3 = Curso("Inglés 1", "ing1")
curso_4 = Curso("Inglés 2", "ing2")
curso_5 = Curso("Laboratorio 1", "lab1")
curso_6 = Curso("Laboratorio 2", "lab2")
    
listado_cursos = [curso_1,curso_2, curso_3, curso_4, curso_5, curso_6 ]