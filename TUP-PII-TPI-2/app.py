import os
from estudiante import *
from profesor import *
from datospersonales import *


def menu():
    print("----------------------------------------")
    print("|1 - Ingresar cómo alumno              |")
    print("|2 - Ingresar cómo profesor            |")
    print("|3 - Ver cursos                        |")
    print("|4 - Salir                             |")
    print("----------------------------------------\n")


print("---------------")
print("| BIENVENIDO! |")
print("---------------\n")
respuesta = ""

while respuesta != "salir":
    menu()
    opt = input("Ingrese la opción de menú: ")

    if opt.isnumeric():
        opt = int(opt)
        if opt == 1:
            mail_ingresado = input("ingrese su email: ")
            contrasenia_ingresada = input("Ingrese la contraseña: ")
            email_encontrado = False
            for objeto in registro:
                # if objeto.validar_credenciales(mail_ingresado, contrasenia_ingresada):
                # no funciona validar_credenciales() sin chequear que el objeto sea una instancia de estudiante o profesor
                if isinstance(objeto, (Estudiante, Profesor)) and objeto.validar_credenciales(mail_ingresado, contrasenia_ingresada):
                    email_encontrado = True
                    print("Acceso concedido MENSAJE TEMPORAL")
                    
                    print("----------------------------------------")
                    print("|1 - Matricularse a un curso           |")
                    print("|2 - Ver curso                         |")
                    print("|3 - Volver al menú principal          |")
                    print("----------------------------------------\n")       
                    
                    respuesta_submenu = ""
                    while respuesta_submenu != "salir":
                        opt_submenu_alumno = input("Ingrese la opción de menú: ")
                        if opt_submenu_alumno.isnumeric():
                            opt_submenu_alumno= int(opt_submenu_alumno)
                        if opt_submenu_alumno == 1:
                            #mostrar cursos
                            pass
                            
                            

            if not email_encontrado:
                os.system("clear")  # cambiar a cls para windows
                print("------------------------------------------------------")
                print("| Mail no registrado, debe darse de alta en alumnado |")
                print("------------------------------------------------------\n")

        elif opt == 2:
            mail_ingresado = input("ingrese su email:   ")
            contrasenia_ingresada = input("Ingrese la contraseña:   ")
            email_encontrado = False
            for objeto in registro:
                if isinstance(objeto, (Estudiante, Profesor)) and objeto.validar_credenciales(mail_ingresado, contrasenia_ingresada):
                    email_encontrado = True
                    print("Acceso concedido MENSAJE TEMPORAL")
                    break

            if not email_encontrado:
                os.system("clear")  # cambiar a cls para windows
                print("------------------------------------------------------")
                print("| Mail no registrado, debe darse de alta en alumnado |")
                print("------------------------------------------------------\n")
        elif opt == 3:
            """cursos_ordenados = sorted(cursos, key=itemgetter("Materia"))
            for cursos in cursos_ordenados:
                print(cursos)"""

        elif opt == 4:
            os.system("clear")  # cambiar a cls para windows
            print("--------------------")
            print("| FIN DEL PROGRAMA |")
            print("--------------------\n")
            respuesta = "salir"
        else:
            print("----------------------------------------")
            print("| No ha ingresado una opción válida... |")
            print("----------------------------------------\n")
    else:
        print("----------------------------------")
        print("| Ingrese una opción numérica... |")
        print("----------------------------------\n")
