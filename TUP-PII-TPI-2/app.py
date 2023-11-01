import os
import datos
import funciones

# datos útiles para pruebas rápidas:

# usuario nombre: test Estudiante, mail 1 contraseña 2
# inscripto en carrera: "Tecnicatura Universitaria en programación"

# usuario test Profesor, mail 2 contraseña 3

# el admin code es: admin123

# el programa inicia sin cursos en el sistema, solo con la carrera " Tecnicatura Universitaria en programación" que tiene 1 alumno inscripto(test Estudiante)

funciones.mensaje_bienvenida()

while True:
    opt = funciones.menu_principal()
    if opt == 1:
        objeto_activo = funciones.prompt_datos_validar_credenciales(opt)
        if objeto_activo:
            while True:
                opt_alumno = funciones.menu_alumno()
                os.system("cls")
                if opt_alumno == 1:
                    funciones.prompt_matricular(objeto_activo)
                elif opt_alumno == 2:
                    funciones.prompt_desmatricular(objeto_activo)
                elif opt_alumno == 3:
                    funciones.imprimir_cursos_inscripto(objeto_activo)
                elif opt_alumno == 4:
                    break
    elif opt == 2:
        objeto_activo = funciones.prompt_datos_validar_credenciales(opt)
        if not objeto_activo:
            alta_profesor = funciones.alta_profesor()
        else:
            while True:
                opt_profesor = funciones.menu_profesor()
                os.system("cls")
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
        break
