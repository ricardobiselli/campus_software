import os
from curso import *
from datospersonales import *


def menu_principal():
    print("----------------------------------------")
    print("|1 - Ingresar cómo alumno              |")
    print("|2 - Ingresar cómo profesor            |")
    print("|3 - Ver cursos                        |")
    print("|4 - Salir                             |")
    print("----------------------------------------\n")


def mensaje_bienvenida():
    print("---------------")
    print("| BIENVENIDO! |")
    print("---------------\n")


def mensaje_acceso_concedido():
    print("--------------------")
    print("| Acceso concedido!|")
    print("--------------------\n")


def menu_alumno():
    print("----------------------------------------")
    print("|1 - Matricularse a un curso           |")
    print("|2 - Ver curso                         |")
    print("|3 - Volver al menú principal          |")
    print("----------------------------------------\n")


def menu_listado_cursos():
    index = 0
    print("---------------------")
    for curso in listado_cursos:
        print(f"{index + 1}- {curso.nombre}")
        index += 1
    print("---------------------\n")


def prompt_datos_validar_credenciales():
    mail_ingresado = input("Ingrese su email: ")
    contrasenia_ingresada = input("Ingrese la contraseña: ")
    acceso_validado = False
    objeto_activo = None

    for objeto in registro:
        if isinstance(objeto, (Estudiante, Profesor)) and objeto.validar_credenciales(mail_ingresado, contrasenia_ingresada):
            acceso_validado = True
            objeto_activo = objeto
            os.system("clear")  # cambiar a cls para Windows
            
            break  

    if acceso_validado:
        mensaje_acceso_concedido()
    return objeto_activo



def prompt_matricular(objeto_activo):
    opt_submenu_matriculacion = input(
        "Ingrese el número de curso al que desea matricularse: ")
    if opt_submenu_matriculacion.isnumeric():
        opt_submenu_matriculacion = int(opt_submenu_matriculacion)
        if 1 <= opt_submenu_matriculacion <= 6:
            curso_a_matricularse = listado_cursos[opt_submenu_matriculacion - 1]
            if curso_a_matricularse in objeto_activo._mis_cursos:
                os.system("clear")  # cambiar a cls para Windows
                mensaje_error_matriculacion()
                menu_listado_cursos()
            else:
                matricula_ingresada = input(
                    "Ingrese la clave de matriculación: ")
                if matricula_ingresada == listado_cursos[opt_submenu_matriculacion - 1].contrasenia_matriculacion:
                    objeto_activo._mis_cursos.append(curso_a_matricularse)
                    for curso in objeto_activo._mis_cursos:
                        os.system("clear")  # cambiar a cls para Windows
                        mensaje_matricula_exitosa(curso)


def mensaje_error_matriculacion():
    print("------------------------------------------------")
    print("| Ya se encuentra matriculado en este curso... |")
    print("------------------------------------------------\n")


def mensaje_matricula_exitosa(curso):
    print("-------------------------------------------------------")
    print(f" Se ha matriculado exitosamente en: {curso.nombre}   ")
    print("-------------------------------------------------------\n")


def imprimir_cursos_inscripto(curso, objeto):
    print("Estos son todos tus cursos:\n")
    print("-------------------")
    index = 0
    for curso in objeto._mis_cursos:
        print(f"{index + 1} - {curso.nombre}")
    print("-------------------\n")


def mensaje_opcion_numero_invalido():
    print("----------------------------------------")
    print("| No ha ingresado una opción válida... |")
    print("----------------------------------------\n")


def mensaje_opcion_debe_ser_numerica():
    print("----------------------------------")
    print("| Ingrese una opción numérica... |")
    print("----------------------------------\n")


def mensaje_mail_no_registrado():
    print("------------------------------------------------------")
    print("| Mail no registrado, debe darse de alta en alumnado |")
    print("------------------------------------------------------\n")


def mensaje_fin_programa():
    print("--------------------")
    print("| FIN DEL PROGRAMA |")
    print("--------------------\n")
    respuesta = "salir"