import os
from estudiante import *
from profesor import *
from datospersonales import *
from funciones import *

mensaje_bienvenida()

# bucle externo sin validaciones temporalmente
opt = 0
while opt != 4:
    menu_principal()
    opt = input("Ingrese la opción del menú: ")
    opt = int(opt)
    if opt == 1:
        objeto_activo = prompt_datos_validar_credenciales()
        while True:
            if objeto_activo:
                menu_alumno()
                opt_alumno = input("Ingrese la opción del menú: ")
                opt_alumno = int(opt_alumno)
                os.system("clear")

                if opt_alumno == 1:
                    menu_listado_cursos()
                    prompt_matricular(objeto_activo)
                elif opt_alumno == 2:
                    imprimir_cursos_inscripto(objeto_activo)
                elif opt_alumno == 3:
                    break  # vuelta al menu_principal
                else:
                    mensaje_opcion_numero_invalido()
            else:
                mensaje_mail_no_registrado()
                break
    elif opt == 2:
        pass
    elif opt == 3:
        pass
    elif opt == 4:
        os.system("clear")  # cambiar a cls para Windows
        mensaje_fin_programa()
