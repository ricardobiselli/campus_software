import os
from estudiante import *
from profesor import *
from datospersonales import *
from funciones import *

mensaje_bienvenida()

opt = 0
while opt != 4:
    menu_principal()
    opt = input("Ingrese la opción del menú: ")
    if opt.isdigit():
        opt = int(opt)
        if 1 <= opt <= 4:
            if opt == 1:
                objeto_activo = prompt_datos_validar_credenciales(opt)
                while True:
                    if objeto_activo:
                        menu_alumno()
                        opt_alumno = input("Ingrese la opción del menú: ")
                        if opt_alumno.isdigit():
                            opt_alumno = int(opt_alumno)
                            if 1 <= opt_alumno <= 3:
                                os.system("clear")

                                if opt_alumno == 1:
                                    menu_listado_cursos()
                                    prompt_matricular(objeto_activo)
                                elif opt_alumno == 2:
                                    imprimir_cursos_inscripto(objeto_activo)
                                elif opt_alumno == 3:
                                    break
                            else:
                                mensaje_opcion_numero_invalido()
                        else:
                            mensaje_opcion_debe_ser_numerica()
            elif opt == 2:
                objeto_activo = prompt_datos_validar_credenciales(opt)
                while True:
                    if objeto_activo:
                        menu_profesor()
                        opt_profesor = input("Ingrese la opción del menú: ")
                        if opt_profesor.isdigit():
                            opt_profesor = int(opt_profesor)
                            if 1 <= opt_profesor <= 3:
                                os.system("clear")
                                if opt_profesor == 1:
                                    nuevo_curso = crear_nuevo_curso(objeto_activo)
                                elif opt_profesor == 2:
                                    imprimir_cursos_inscripto(objeto_activo)
                                elif opt_profesor == 3:
                                    break
                            else:
                                mensaje_opcion_numero_invalido()
                        else:
                            mensaje_opcion_debe_ser_numerica()
            elif opt == 3:
                pass
            elif opt == 4:
                mensaje_fin_programa()
        else:
            mensaje_opcion_numero_invalido()
    else:
        mensaje_opcion_debe_ser_numerica()
