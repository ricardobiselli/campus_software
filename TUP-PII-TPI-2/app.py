import os
import datospersonales
import funciones

funciones.mensaje_bienvenida()

opt = 0
while opt != 4:
    funciones.menu_principal()
    opt = input("Ingrese la opción del menú: ")
    if opt.isdigit():
        opt = int(opt)
        if 1 <= opt <= 4:
            if opt == 1:
                objeto_activo = funciones.prompt_datos_validar_credenciales(
                    opt)
                while True:
                    if objeto_activo:
                        funciones.menu_alumno()
                        opt_alumno = input("Ingrese la opción del menú: ")
                        if opt_alumno.isdigit():
                            opt_alumno = int(opt_alumno)
                            if 1 <= opt_alumno <= 3:
                                os.system("clear")

                                if opt_alumno == 1:
                                    funciones.menu_listado_cursos()
                                    funciones.prompt_matricular(objeto_activo)
                                elif opt_alumno == 2:
                                    funciones.imprimir_cursos_inscripto(
                                        objeto_activo)
                                elif opt_alumno == 3:
                                    break
                            else:
                                funciones.mensaje_opcion_numero_invalido()
                        else:
                            funciones.mensaje_opcion_debe_ser_numerica()
            elif opt == 2:
                objeto_activo = funciones.prompt_datos_validar_credenciales(
                    opt)
                while True:
                    if objeto_activo:
                        funciones.menu_profesor()
                        opt_profesor = input("Ingrese la opción del menú: ")
                        if opt_profesor.isdigit():
                            opt_profesor = int(opt_profesor)
                            if 1 <= opt_profesor <= 3:
                                os.system("clear")
                                if opt_profesor == 1:
                                    nuevo_curso = funciones.crear_nuevo_curso(
                                        objeto_activo)
                                elif opt_profesor == 2:
                                    funciones.imprimir_cursos_inscripto(
                                        objeto_activo)
                                elif opt_profesor == 3:
                                    break
                            else:
                                funciones.mensaje_opcion_numero_invalido()
                        else:
                            funciones.mensaje_opcion_debe_ser_numerica()
                    else:
                        if not objeto_activo:
                            if funciones.alta_profesor() == True:
                                break
            elif opt == 3:
                cursos_ordenados = funciones.ordenar_cursos(
                    datospersonales.listado_cursos)
                funciones.mostrar_cursos_ordenados(cursos_ordenados)
            elif opt == 4:
                funciones.mensaje_fin_programa()
        else:
            funciones.mensaje_opcion_numero_invalido()
    else:
        funciones.mensaje_opcion_debe_ser_numerica()
