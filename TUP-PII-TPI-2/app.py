import os
from estudiante import *
from profesor import *
from datospersonales import *
from curso import listado_cursos
from funciones import *

mensaje_bienvenida()

respuesta = ""

while respuesta != "salir":  
    menu_principal()  
    opt = input("Ingrese la opción de menú: ")
    if opt.isnumeric():
        opt = int(opt)
        if opt == 1:
            mail_ingresado = input("Ingrese su email: ")
            contrasenia_ingresada = input("Ingrese la contraseña: ")
            email_encontrado = False
            for objeto in registro:
                if isinstance(objeto, (Estudiante, Profesor)) and objeto.validar_credenciales(mail_ingresado, contrasenia_ingresada):
                    email_encontrado = True
                    os.system("clear")  # cambiar a cls para Windows                    
                    mensaje_acceso_concedido()                   
                    respuesta_submenu = ""
                    while respuesta_submenu != "salir":         
                        menu_alumno()                  
                        opt_submenu_alumno = input("Ingrese la opción de menú: ")
                        os.system("clear")
                        if opt_submenu_alumno.isnumeric():
                            opt_submenu_alumno = int(opt_submenu_alumno)
                            if opt_submenu_alumno == 1:                              
                                menu_listado_cursos()                               
                                respuesta_submenu_alumno = ""
                                while respuesta_submenu_alumno != "salir":
                                    opt_submenu_matriculacion = input("Ingrese el número de curso al que desea matricularse: ")
                                    if opt_submenu_matriculacion.isnumeric():
                                        opt_submenu_matriculacion = int(opt_submenu_matriculacion)
                                        if 1 <= opt_submenu_matriculacion <= 6:
                                            curso_a_matricularse = listado_cursos[opt_submenu_matriculacion - 1]
                                            if curso_a_matricularse in objeto._mis_cursos: 
                                                os.system("clear")  # cambiar a cls para Windows                                                  
                                                mensaje_error_matriculacion()
                                                menu_listado_cursos()                                               
                                            else:
                                                matricula_ingresada = input("Ingrese la clave de matriculación: ")
                                                if matricula_ingresada == listado_cursos[opt_submenu_matriculacion - 1].contrasenia_matriculacion:
                                                    objeto._mis_cursos.append(curso_a_matricularse)
                                                    for curso in objeto._mis_cursos:
                                                        os.system("clear")  # cambiar a cls para Windows                                                      
                                                        mensaje_matricula_exitosa(curso)                    
                                                break
                            elif opt_submenu_alumno == 2:         
                                imprimir_cursos_inscripto(curso, objeto) #ERROR??? 
                            elif opt_submenu_alumno == 3:
                                respuesta_submenu = "salir"  
                            else:  
                                mensaje_opcion_numero_invalido()
                        else:  
                            mensaje_opcion_debe_ser_numerica()     
                    if not email_encontrado:
                        os.system("clear")  # cambiar a cls para Windows
                        mensaje_mail_no_registrado()              
        elif opt == 2:
            mail_ingresado = input("Ingrese su email: ")
            contrasenia_ingresada = input("Ingrese la contraseña: ")
            email_encontrado = False
            for objeto in registro:
                if isinstance(objeto, (Estudiante, Profesor)) and objeto.validar_credenciales(mail_ingresado, contrasenia_ingresada):
                    email_encontrado = True
                    print("Acceso concedido MENSAJE TEMPORAL")
                    break
            if not email_encontrado:
                os.system("clear")  # cambiar a cls para Windows
                print("------------------------------------------------------")
                print("| Mail no registrado, debe darse de alta en alumnado |")
                print("------------------------------------------------------\n")
        elif opt == 3:
            pass
        elif opt == 4:
            os.system("clear")  # cambiar a cls para Windows
            mensaje_fin_programa()
        else:
            print("----------------------------------------")
            print("| No ha ingresado una opción válida... |")
            print("----------------------------------------\n")
    else:
        print("----------------------------------")
        print("| Ingrese una opción numérica... |")
        print("----------------------------------\n")
