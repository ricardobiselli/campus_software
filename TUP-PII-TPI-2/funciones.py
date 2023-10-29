import os
import curso
import datos
import estudiante
import profesor


def prompt_datos_validar_credenciales(opt):
    while True:
        mail_ingresado = input("Ingrese su email: ")
        contrasenia_ingresada = input("Ingrese la contraseña: ")
        objeto_activo = None
        if opt == 1:
            for objeto in datos.registro:
                if isinstance(objeto, estudiante.Estudiante) and objeto.email == mail_ingresado:
                    if objeto.contrasenia == contrasenia_ingresada:
                        acceso_validado = objeto.validar_credenciales(
                            mail_ingresado, contrasenia_ingresada)
                        if acceso_validado:
                            os.system("clear")
                            mensaje_acceso_concedido()
                        objeto_activo = objeto
                    else:
                        os.system("clear")
                        mensaje_contrasenia_invalida()
                else:
                    os.system("clear")
                    mensaje_mail_no_registrado()
        elif opt == 2:
            for objeto in datos.registro:
                if isinstance(objeto, profesor.Profesor) and objeto.email == mail_ingresado:
                    if objeto.contrasenia == contrasenia_ingresada:
                        acceso_validado = objeto.validar_credenciales(
                            mail_ingresado, contrasenia_ingresada)
                        os.system("clear")
                        mensaje_acceso_concedido()
                        objeto_activo = objeto
                    else:
                        os.system("clear")
                        mensaje_contrasenia_invalida()
                else:
                    os.system("clear")
                    mensaje_mail_no_registrado()
        if objeto_activo:
            return objeto_activo
        else:
            return False


def alta_profesor():
    while True:
        codigo_admin = "admin123"
        print("--------------------------------------------------------------------------------------------------")
        print("|Ingrese el código de administrador para darse de alta en el sistema o 'exit' para volver atrás...|")
        print("---------------------------------------------------------------------------------------------------\n")
        codigo_admin_ingresado = input("Ingrese el código de administrador: ")
        if codigo_admin_ingresado == codigo_admin:
            os.system("clear")
            nombre_nuevo_profesor = input("Ingrese su nombre: ")
            apellido_nuevo_profesor = input("Ingrese su apellido: ")
            email_nuevo_profesor = input("Ingrese su email: ")
            password_nuevo_profesor = input("Ingrese su contraseña: ")
            titulo_nuevo_profesor = input("Ingrese su título: ")
            anio_nuevo_profesor = input("Ingrese año de egreso: ")

            objeto_nuevo_profesor = profesor.Profesor(titulo_nuevo_profesor, anio_nuevo_profesor,
                                                      nombre_nuevo_profesor, apellido_nuevo_profesor, email_nuevo_profesor, password_nuevo_profesor)
            datos.registro.append(objeto_nuevo_profesor)
            os.system("clear")
            print("se ha dado de alta un nuevo profesor con estos datos:\n")
            print(F"nombre: {nombre_nuevo_profesor}")
            print(F"apellido: {apellido_nuevo_profesor}")
            print(F"titulo: {titulo_nuevo_profesor}")
            print(F"año de egreso: {anio_nuevo_profesor}")
            print(F"email: {email_nuevo_profesor}")
            print(F"contraseña: {password_nuevo_profesor}\n")
            print("registro exitoso, volviendo al menu principal...\n")
            break
        else:
            os.system("clear")
            print("--------------------------------------------------------------------")
            print("|código de administrador incorrecto, volviendo al menú principal...|")
            print("--------------------------------------------------------------------\n")
            break
    return True

def prompt_matricular(objeto_activo):
    opt = ""
    while opt != "break":
        opt = input(
            "Ingrese el número de curso al que desea matricularse: ")
        if opt.isnumeric():
            opt = int(opt)
            if 1 <= opt <= len(curso.listado_cursos):
                curso_a_matricularse = curso.listado_cursos[opt - 1]
                if curso_a_matricularse in objeto_activo._mis_cursos:
                    os.system("clear")  # cambiar a clear para Windows
                    mensaje_error_matriculacion()
                    menu_listado_cursos()
                else:
                    matricula_ingresada = input(
                        "Ingrese la clave de matriculación: ")
                    if matricula_ingresada == curso.listado_cursos[opt - 1]._contrasenia_matriculacion:
                        objeto_activo.matricular_en_curso(
                            objeto_activo, curso_a_matricularse)  # ????
                        opt = "break"

                        os.system("clear")  # cambiar a clear para Windows
                        mensaje_matricula_exitosa(curso_a_matricularse)
                    else:
                        mensaje_contrasenia_invalida()  # matricula inválida
            else:
                mensaje_opcion_numero_invalido()
                menu_listado_cursos()
        else:
            mensaje_opcion_debe_ser_numerica()
            menu_listado_cursos()


def menu_listado_cursos():
    index = 0
    print("---------------------")
    for cursoItem in curso.listado_cursos:
        print(f"{index + 1}- {cursoItem._nombre}")
        index += 1
    print("---------------------\n")


def imprimir_cursos_inscripto(objeto_activo):
    while objeto_activo._mis_cursos:
        print("Estos son todos tus cursos:\n")
        print("-------------------")

        indice = 0
        for curso in objeto_activo.mis_cursos:
            indice += 1
            print(f"{indice} - {curso._nombre}")
        print("-------------------\n")

        curso_seleccionado = input(
            "Ingrese la opción correspondiente a uno de los cursos: ")
        if curso_seleccionado.isnumeric():
            indice = int(curso_seleccionado) - 1
            if 0 <= indice < len(objeto_activo.mis_cursos):
                curso_seleccionado = objeto_activo.mis_cursos[indice]
                print(f"Nombre: {curso_seleccionado._nombre}")
                if isinstance(objeto_activo, profesor.Profesor):
                    print(
                        f"Nombre: {curso_seleccionado._nombre} cod. matriculación: {curso_seleccionado._contrasenia_matriculacion}")
                break
            else:
                mensaje_opcion_numero_invalido()
        else:
            mensaje_opcion_debe_ser_numerica()
    if not objeto_activo.mis_cursos:
        print("------------------------------")
        print("| No posee cursos activos... |")
        print("------------------------------\n")


def crear_nuevo_curso(objeto_activo):
    indice = 0
    for carrera in datos.listado_carreras:
        print(f"{indice +1}{carrera._nombre}")
        indice += 1
        if indice == len(datos.listado_carreras):
            break
    numero_carrera = input("Ingrese el nro de la carrera que desea elegir:")
    carrera_elegida = datos.listado_carreras[int(numero_carrera)-1]._nombre
    nombre_nuevo_curso = input("Ingrese el nombre del curso que desea crear:")
    for cur in carrera_elegida:
        if cur == nombre_nuevo_curso:
            print("-------------------------------------------------------------------------------------------------------")
            print(f"| Este curso ya está disponible en la carrera {carrera_elegida._nombre}, no puede agregarlo nuevamente|")
            print("-------------------------------------------------------------------------------------------------------\n")
        else:           
            contrasenia_nuevo_curso = curso.Curso.generar_contrasenia()
            nuevo_objeto_curso = curso.Curso(
                nombre_nuevo_curso, contrasenia_nuevo_curso)
            objeto_activo.dictar_curso(objeto_activo, nuevo_objeto_curso)

    print("---------------------------------------------------------------------------------------------")
    print(
        f" Ha agregado exitosamente el curso '{nombre_nuevo_curso}', clave mat: '{contrasenia_nuevo_curso}'")
    print("---------------------------------------------------------------------------------------------\n")


def ordenar_cursos(listado):
    listado_cursos_ordenados = sorted(listado, key=lambda x: x._nombre)
    return listado_cursos_ordenados


def mostrar_cursos_ordenados(listado_ordenado):
    for curso in listado_ordenado:
        print(
            f"Materia: {curso._nombre} Carrera: Tecnicatura Universitaria en Programación")
    print("------------------------------\n")


"""def opcion_alta_profesor():
    while True:"""


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
    print("|1 - Desmatricularse a un curso        |")
    print("|2 - Ver curso                         |")
    print("|3 - Volver al menú principal          |")
    print("----------------------------------------\n")


def menu_profesor():
    print("----------------------------------------")
    print("|1 - Dictar curso                      |")
    print("|2 - Ver curso                         |")
    print("|3 - Volver al menú principal          |")
    print("----------------------------------------\n")


def mensaje_error_matriculacion():
    print("------------------------------------------------")
    print("| Ya se encuentra matriculado en este curso... |")
    print("------------------------------------------------\n")


def mensaje_matricula_exitosa(curso):
    print("-------------------------------------------------------")
    print(f" Se ha matriculado exitosamente en: {curso._nombre}   ")
    print("-------------------------------------------------------\n")


def mensaje_opcion_numero_invalido():
    os.system("clear")
    print("----------------------------------------")
    print("| No ha ingresado una opción válida... |")
    print("----------------------------------------\n")


def mensaje_opcion_debe_ser_numerica():
    os.system("clear")
    print("----------------------------------")
    print("| Ingrese una opción numérica... |")
    print("----------------------------------\n")


def mensaje_mail_no_registrado():
    os.system("clear")  # cambiar a clear para Windows
    print("------------------------------------------------------")
    print("| Mail no registrado, debe darse de alta en alumnado |")
    print("------------------------------------------------------\n")


def mensaje_contrasenia_invalida():
    print("------------------------------")
    print("| contrasenia inválida   ... |")
    print("------------------------------\n")


def mensaje_fin_programa():
    os.system("clear")
    print("--------------------")
    print("| FIN DEL PROGRAMA |")
    print("--------------------\n")
