import os
from estudiante import *
from profesor import *
from datospersonales import *
from curso import listado_cursos
from funciones import *

mensaje_bienvenida()

opt = 0
while opt != 4: 
    menu_principal()  
    opt = input("Ingrese la opción de menú: ")
    opt = int(opt) 
    if opt == 1:
        prompt_datos_validar_credenciales()
            
        menu_alumno()                  
        opt_alumno = input("Ingrese la opción de menú: ")
        opt_alumno = int(opt_alumno)
        os.system("clear")
            
        if opt_alumno == 1:
            menu_listado_cursos()
            prompt_matricular(prompt_datos_validar_credenciales())       
                
        elif opt_alumno == 2:
            pass #imprimir_cursos_inscripto(curso, objeto) # ERROR???
        elif opt_alumno == 3:
            respuesta_submenu = "salir"  
        else:  
            mensaje_opcion_numero_invalido()
                #else:  
                #    mensaje_opcion_debe_ser_numerica()     
        #if not email_encontrado:
        #    os.system("clear")  # cambiar a cls para Windows
        #    mensaje_mail_no_registrado()              
    elif opt == 2:
        pass
    elif opt == 3:
        pass
    elif opt == 4:
        os.system("clear")  # cambiar a cls para Windows
        mensaje_fin_programa()
   
