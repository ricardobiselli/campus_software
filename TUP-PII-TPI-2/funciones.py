import os
from curso import *


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


#def matriculacion(objeto):
#    pass
    


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
