import os
from estudiante import *
from datospersonales import *
from operator import itemgetter


def menu():
    print("|--------------------------------------|")
    print("|1 - Ingresar cómo alumno              |")
    print("|2 - Ingresar cómo profesor            |")
    print("|3 - Ver cursos                        |")
    print("|4 - Salir                             |")
    print("|--------------------------------------|\n")


print("Bienvenido!")
respuesta = ""

while respuesta != "salir":
    menu()
    opt = input("Ingrese la opción de menú: ")

    if opt.isnumeric():
        opt = int(opt)
        if opt == 1:   
            mail_ingresado = input("ingrese su email: ")
            contrasenia_ingresada = input("Ingrese la contraseña: ")            
            resultado = Usuario.validar_credenciales(alumnos, mail_ingresado, contrasenia_ingresada)

            if resultado:
                print("Acceso permitido")
            else:
                print("Acceso denegado")
        elif opt == 2:
                mail_ingresado = input("ingrese su email: ")
                contrasenia_ingresada = input("Ingrese la contraseña: ")
                resultado = Usuario.validar_credenciales(profesores, mail_ingresado, contrasenia_ingresada)
           
        elif opt == 3:
            cursos_ordenados = sorted(cursos, key=itemgetter("Materia"))  
            for cursos in cursos_ordenados: 
                print (cursos) 
               
        elif opt == 4:
            os.system("clear")  # cambiar a cls para windows
            print("Saliendo del programa.")
            respuesta = "salir"
        else:
            print("No ha ingresado una opción válida")
    else:
        print("Ingrese una opción numérica")
