from profesor import *
from estudiante import *
from carrera import *

registro = [
    Estudiante(53013, 2023, "Ricardo", "Biselli", "ricardobiselli@gmail.com", "131313"),
    Estudiante(
        11111, 2023, "usuario de prueba nombre", "usuario de prueba apellido", "1", "2"
    ),  # mail: 1 password: 2 para hacer pruebas rápidas
    Profesor(
        "full stack developer",
        2010,
        "Mercedes",
        "Valoni",
        "mercedes@gmail.com",
        "mercedes123",
    ),
    Profesor(
        "sysadmin",
        2011,
        "juan",
        "perez",  # mail: 2 password: 3 para hacer pruebas rápidas
        "2",
        "3",
    ),
]

carrera1 = Carrera("Tecnicatura Universitaria en Programación", 2)
carrera2 = Carrera("otra carrera test", 2)

listado_carreras = []

listado_carreras.append(carrera1)
listado_carreras.append(carrera2)

carrera1.add_curso(listado_cursos[0])
carrera1.add_curso(listado_cursos[1])
carrera1.add_curso(listado_cursos[2])
carrera1.add_curso(listado_cursos[3])
carrera1.add_curso(listado_cursos[4])
carrera1.add_curso(listado_cursos[5])

carrera2.add_curso(listado_cursos[1])


carrera1.add_alumno(registro[1])
