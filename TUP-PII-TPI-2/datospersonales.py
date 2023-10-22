from profesor import *
from estudiante import *

registro = [
    Estudiante(53013, 2023, "Ricardo", "Biselli",
               "ricardobiselli@gmail.com", "131313"), 
    Estudiante(11111,2023, "usuario de prueba nombre", "usuario de prueba apellido", "1","2"), # mail: 1 password: 2 para hacer pruebas rápidas
    Profesor("full stack developer", 2010, "Mercedes", "Valoni",
             "mercedes@gmail.com", "mercedes123"),  
    Profesor("sysadmin", 2011, "juan", "perez",# mail: 2 password: 3 para hacer pruebas rápidas
             "2", "3"),  
]

"""Al estar hardcodeados no hay forma de chequear que no se repita un mail, podría iterar 
sobre el registro para buscar repetidos y mostrar una advertencia ? o hacer esa iteración 
al inicio del programa y forzar la salida si encuentra repetidos"""