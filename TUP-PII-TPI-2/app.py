import os
import datos
import funciones

funciones.mensaje_bienvenida()

opt = 0 
while opt != 4:
    opt = funciones.menu_principal()
    if opt == 1:
        objeto_activo = funciones.prompt_datos_validar_credenciales(opt)
        if objeto_activo:
            opt_alumno = funciones.menu_alumno()
            os.system("clear")
            if opt_alumno == 1:
                funciones.menu_listado_cursos()
                funciones.prompt_matricular(objeto_activo)
            elif opt_alumno == 2:
                funciones.imprimir_cursos_inscripto(objeto_activo)
            elif opt_alumno == 3:
                pass
            elif opt_alumno == 4:
                break
    elif opt == 2:
        objeto_activo = funciones.prompt_datos_validar_credenciales(opt)
        if not objeto_activo:
            alta_profesor = funciones.alta_profesor()
            if alta_profesor:
                funciones.mensaje_acceso_concedido() 
        else:  
            opt_profesor = funciones.menu_profesor()
            os.system("clear")
            if opt_profesor == 1:
                nuevo_curso = funciones.crear_nuevo_curso(objeto_activo)
            elif opt_profesor == 2:
                funciones.imprimir_cursos_inscripto(objeto_activo)
            elif opt_profesor == 3:
                break
    elif opt == 3:
        cursos_ordenados = funciones.ordenar_cursos(datos.listado_cursos)
        funciones.mostrar_cursos_ordenados(cursos_ordenados)
    elif opt == 4:
        funciones.mensaje_fin_programa()
