import os
import curso
import datos
import estudiante
import profesor
from archivo import Archivo


def prompt_datos_validar_credenciales(opt):
    while True:
        mail_ingresado = input("Ingrese su email: ")
        contrasenia_ingresada = input("Ingrese la contraseña: ")
        objeto_activo = None
        if opt == 1:
            for objeto in datos.registro:
                if (
                    isinstance(objeto, estudiante.Estudiante)
                    and objeto.email == mail_ingresado
                ):
                    if objeto.contrasenia == contrasenia_ingresada:
                        acceso_validado = objeto.validar_credenciales(
                            mail_ingresado, contrasenia_ingresada
                        )
                        if acceso_validado:
                            os.system("cls")
                            objeto_activo = objeto  # login exitoso!
                            mensaje_acceso_concedido(objeto_activo)
                        break
                    else:
                        os.system("cls")
                        mensaje_contrasenia_invalida()
                        return  # vuelta al menu principal ante mail correcto pero contraseña inválida
            else:
                os.system("cls")
                mensaje_mail_no_registrado()
                return  # vuelta al menu principal ante mail no registrado

        elif opt == 2:
            for objeto in datos.registro:
                if (
                    isinstance(objeto, profesor.Profesor)
                    and objeto.email == mail_ingresado
                ):
                    if objeto.contrasenia == contrasenia_ingresada:
                        acceso_validado = objeto.validar_credenciales(
                            mail_ingresado, contrasenia_ingresada
                        )
                        os.system("cls")
                        objeto_activo = objeto
                        mensaje_acceso_concedido(objeto_activo)

                        break
                    else:
                        os.system("cls")
                        mensaje_contrasenia_invalida()
                        break
            else:
                os.system("cls")
                mensaje_mail_no_registrado()
                return False  # False permite entrar a la funcion para registro de profesor en la app
        if objeto_activo:
            return objeto_activo  # permite que la app continue con el submenu profesor


def alta_profesor():
    codigo_admin = "admin123"
    print(
        "-------------------------------------------------------------------------------------------"
    )
    print(
        "|Ingrese el código de administrador para darse de alta en el sistema o ENTER para salir...|"
    )
    print(
        "-------------------------------------------------------------------------------------------\n"
    )
    codigo_admin_ingresado = input("Ingrese el código de administrador: ")
    if codigo_admin_ingresado == codigo_admin:
        os.system("cls")
        nombre_nuevo_profesor = input("Ingrese su nombre: ")
        apellido_nuevo_profesor = input("Ingrese su apellido: ")
        email_nuevo_profesor = input("Ingrese su email: ")
        password_nuevo_profesor = input("Ingrese su contraseña: ")
        titulo_nuevo_profesor = input("Ingrese su título: ")
        anio_nuevo_profesor = input("Ingrese año de egreso: ")

        objeto_nuevo_profesor = profesor.Profesor( # instanciar nuevo objeto clase Profesor
            titulo_nuevo_profesor,
            anio_nuevo_profesor,
            nombre_nuevo_profesor,
            apellido_nuevo_profesor,
            email_nuevo_profesor,
            password_nuevo_profesor,
        )
        datos.registro.append(objeto_nuevo_profesor)
        os.system("cls")
        print("se ha dado de alta un nuevo profesor con estos datos:\n")
        print(f"nombre: {nombre_nuevo_profesor}")
        print(f"apellido: {apellido_nuevo_profesor}")
        print(f"titulo: {titulo_nuevo_profesor}")
        print(f"año de egreso: {anio_nuevo_profesor}")
        print(f"email: {email_nuevo_profesor}")
        print(f"contraseña: {password_nuevo_profesor}\n")
        print("registro exitoso, volviendo al menu principal...\n")
        return True
    else:
        os.system("cls")
        print("--------------------------------------------------------------------")
        print("|código de administrador incorrecto, volviendo al menú principal...|")
        print("--------------------------------------------------------------------\n")
        return False


def prompt_matricular(objeto_activo):
    while True:
        if not datos.listado_cursos:
            os.system("cls")
            print("No existen cursos cargados todavía!")
            break
        else:
            sorted_cursos = sorted(datos.listado_cursos, key=lambda curso: curso.codigo) # mostrar cursos ordenados por código

            index = 0
            print("-------------------------------------------------")
            for cursoItem in sorted_cursos:
                print(f"{index + 1}- {cursoItem.nombre} - Código: {cursoItem.codigo}")
                index += 1
            print("-------------------------------------------------\n")
        opt = input("Ingrese el número de curso al que desea matricularse: ")
        if opt.isdigit():
            opt = int(opt)
            if 1 <= opt <= len(datos.listado_cursos):
                curso_a_matricularse = datos.listado_cursos[opt - 1]
                if curso_a_matricularse in objeto_activo.mis_cursos: # validar que el alumno no tenga el curso en su lista
                    os.system("cls")
                    mensaje_error_matriculacion()
                    return
                else:
                    matricula_ingresada = input("Ingrese la clave de matriculación: ")
                    if matricula_ingresada == datos.listado_cursos[opt - 1].contrasenia_matriculacion:
                        objeto_activo.matricular_en_curso(objeto_activo, curso_a_matricularse)
                        os.system("cls")
                        alumno_encontrado = False
                        for carrera in datos.listado_carreras:
                            for alumno in carrera.alumnos:
                                if alumno.nombre == objeto_activo.nombre:
                                    alumno_encontrado = True # validar que alumno pertenece a la carrera
                                    break
                        if alumno_encontrado:
                            mensaje_matricula_exitosa(curso_a_matricularse)
                        else:
                            mensaje_carrera_unregistered()
                            return
                    else:
                        mensaje_contrasenia_invalida()
                        return
                break
            else:
                mensaje_opcion_numero_invalido()
                return
        else:
            mensaje_opcion_debe_ser_numerica()
            return

def prompt_desmatricular(objeto_activo):
    while True:
        if not datos.listado_cursos:
            os.system("cls")
            print("No existen cursos cargados todavía en el sistema!") 
            break
        elif not objeto_activo.mis_cursos:
            os.system("cls")
            print("Usted no está matriculado en ningún curso todavía...")
            break
        else:
            index = 0
            print("------------------------------------")
            for cursoItem in datos.listado_cursos:
                print(f"{index + 1}- {cursoItem.nombre}")
                index += 1
            print("------------------------------------\n")
            opt = input("Ingrese el número del curso al que desea desmatricularse: ")
            if opt.isdigit():
                opt = int(opt)
                if 1 <= opt <= len(datos.listado_cursos):
                    curso_a_desmatricularse = datos.listado_cursos[opt - 1]
                    if curso_a_desmatricularse in objeto_activo.mis_cursos: # desmatricular alumno
                        objeto_activo.desmatricular_curso(
                                objeto_activo, curso_a_desmatricularse
                            )
                        os.system("cls")
                        print("Se ha desmatriculado con exito")
                        break
                    else:
                        mensaje_curso_unregistered()
                        return
                else:
                    mensaje_opcion_numero_invalido()
                    return
            else:
                mensaje_opcion_debe_ser_numerica()
                return
        
def imprimir_cursos_inscripto(objeto_activo):
    while objeto_activo.mis_cursos:
        print("Estos son todos tus cursos:\n") # mostrar cursos para alumno o profesor loggeado, según objeto activo
        print("-------------------")

        indice = 0
        for curso in objeto_activo.mis_cursos:
            indice += 1
            print(f"{indice} - {curso.nombre}")
            if indice >= len(objeto_activo.mis_cursos):
                break
        print("-------------------\n")

        curso_seleccionado = input(
            "Ingrese la opción correspondiente a uno de los cursos: "
        )
        
        if curso_seleccionado.isdigit():
            curso_seleccionado = int(curso_seleccionado)  
            indice_b = curso_seleccionado - 1
            if 0 <= indice_b < len(objeto_activo.mis_cursos): 
                curso_seleccionado = objeto_activo.mis_cursos[indice_b]
                if isinstance(objeto_activo, estudiante.Estudiante): # objeto Estudiante: mostrar curso y archivos ordenados por fecha
                    print("-------------------------------------------")
                    print(f"Nombre: {curso_seleccionado.nombre}\n")
                    print("Archivos del curso ordenados por fecha:")

                    sorted_archivos = sorted(curso_seleccionado.archivos, key=lambda archivo: archivo.fecha)
                    for archivo in sorted_archivos:
                        print(
                            f" - {archivo.nombre} ({archivo.formato}) - fecha: {archivo.fecha}\n"
                        )
                    print("-------------------------------------------")
                    return
                elif isinstance(objeto_activo, profesor.Profesor): # objeto Profesor: mostrar todos los datos del curso y ofrecer agregar más archivos adjuntos
                    print(f"Nombre del curso: {curso_seleccionado.nombre}\n")
                    print(f"Contraseña del curso: {curso_seleccionado.contrasenia_matriculacion}\n")
                    print(f"Código del curso: {curso_seleccionado.codigo}\n")
                    print(f"cantidad de archivos adjuntos: {len(curso_seleccionado.archivos)}\n")
                    
                    respuesta_agregar_curso = input(
                        "Desea agregar un archivo adjunto? si/no: "
                    )
                    while respuesta_agregar_curso.lower() not in ["si", "no"]:
                        print("Por favor, ingrese 'si' o 'no'.")
                        respuesta_agregar_curso = input(
                            "Desea agregar un archivo adjunto? (si/no): "
                        )
                    if respuesta_agregar_curso == "si":
                        nombre_archivo = input(
                            "Ingrese the nombre del archivo adjunto: "
                        )
                        formato_archivo = input(
                            "Ingrese el formato del archivo adjunto, por ejemplo pdf: "
                        )
                        nuevo_objeto_archivo = Archivo(nombre_archivo, formato_archivo)
                        curso_seleccionado.nuevo_archivo(nuevo_objeto_archivo)
                        os.system("cls")
                        print("---------------------------------")
                        print(" Archivo agregado exitosamente!!!  ")
                        print("---------------------------------\n")
                        break
                    else:
                        os.system("cls")
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
    print("Carreras disponibles:")
    for i in range(len(datos.listado_carreras)):
        print(f"{i + 1}. {datos.listado_carreras[i].nombre}")

    while True:
        numero_carrera = input("Ingrese el nro de la carrera que desea elegir: ") #elegir carrera
        if numero_carrera.isnumeric():
            numero_carrera = int(numero_carrera)
            if 1 <= numero_carrera <= len(datos.listado_carreras):
                carrera_elegida = datos.listado_carreras[numero_carrera - 1]
                break
            else:
                print("ERROR, número inválido")
        else:
            print("Por favor, ingrese SOLO NÚMEROS!")
    print("---------------------------------------------------------------")
    print(f"ha seleccionado {carrera_elegida.nombre}")
    print("---------------------------------------------------------------")
    nombre_nuevo_curso = input("Ingrese el nombre del curso que desea crear: ")
    for curso_existente in carrera_elegida.cursos:
        if nombre_nuevo_curso == curso_existente.nombre: # evitar crear curso si ya existe en carrera
            print(
                "----------------------------------------------------------------------------------------------------------------------------"
            )
            print(
                f"| Este curso ya está disponible en la carrera {carrera_elegida.nombre}, no puede agregarlo nuevamente|"
            )
            print(
                "----------------------------------------------------------------------------------------------------------------------------\n"
            )
            return
    else:
        contrasenia_nuevo_curso = curso.Curso.generar_contrasenia()
        nuevo_objeto_curso = curso.Curso(nombre_nuevo_curso, contrasenia_nuevo_curso)
        objeto_activo.dictar_curso(objeto_activo, nuevo_objeto_curso, carrera_elegida) # mandar el curso a los listados correspondientes
    print(
        "--------------------------------------------------------------------------------------------------------"
    )
    print(
       f" Ha agregado exitosamente el curso '{nombre_nuevo_curso}', clave mat: '{contrasenia_nuevo_curso}', código: '{nuevo_objeto_curso.codigo}'"
    )
    print(
        "--------------------------------------------------------------------------------------------------------\n"
    )
    return


def ordenar_cursos(listado):
    listado_cursos_ordenados = sorted(listado, key=lambda x: x.nombre)
    return listado_cursos_ordenados


def mostrar_cursos_ordenados(listado_ordenado):
    if not listado_ordenado:
        os.system("cls")
        print("-------------------------------------------")
        print("| No hay cursos cargados en el sistema... |")
        print("-------------------------------------------\n")
    else:
        for carrera in datos.listado_carreras:
            for curso in listado_ordenado:
                for cursocarrera in carrera.cursos:
                    if cursocarrera.nombre == curso.nombre:
                        print(f"Materia: {curso.nombre} Carrera: {carrera.nombre}")
        print("------------------------------\n")



def menu_principal():
    print("-------------------------------")
    print("|1 - Ingresar cómo alumno     |")
    print("|2 - Ingresar cómo profesor   |")
    print("|3 - Ver cursos               |")
    print("|4 - Salir                    |")
    print("-------------------------------\n")

    opt = input("Ingrese la opción del menú: ")
    if opt.isdigit():
        opt = int(opt)
        if 1 <= opt <= 4:
            return opt
        else:
            mensaje_opcion_numero_invalido()
    else:
        mensaje_opcion_debe_ser_numerica()


def mensaje_bienvenida():
    print("▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
    print("| | | | | | | | | | | | | | | |")

    print(" Por favor agrande la terminal")
    print("    para visualizar mejor")
    print("        el programa      ")
    print("-------------------------------")
    print("|         BIENVENIDO!         |")
    print("-------------------------------\n")


def mensaje_acceso_concedido(objeto_activo):
    print("------------------------------------------------")
    print(f"Acceso concedido! Bienvenido/a: {objeto_activo.nombre}")
    print("------------------------------------------------\n")


def menu_alumno():
    print("----------------------------------------")
    print("|1 - Matricularse a un curso           |")
    print("|2 - Desmatricularse a un curso        |")
    print("|3 - Ver curso                         |")
    print("|4 - Volver al menú principal          |")
    print("----------------------------------------\n")

    opt = input("Ingrese la opción del menú: ")
    if opt.isdigit():
        opt = int(opt)
        if 1 <= opt <= 4:
            return opt
        else:
            mensaje_opcion_numero_invalido()
    else:
        mensaje_opcion_debe_ser_numerica()


def menu_profesor():
    while True:
        print("----------------------------------------")
        print("|1 - Dictar curso                      |")
        print("|2 - Ver curso                         |")
        print("|3 - Volver al menú principal          |")
        print("----------------------------------------\n")

        opt = input("Ingrese la opción del menú: ")
        if opt.isdigit():
            opt = int(opt)
            if 1 <= opt <= 3:
                return opt
            else:
                mensaje_opcion_numero_invalido()
        else:
            mensaje_opcion_debe_ser_numerica()


def mensaje_error_matriculacion():
    print("------------------------------------------------")
    print("| Ya se encuentra matriculado en este curso... |")
    print("------------------------------------------------\n")


def mensaje_matricula_exitosa(curso):
    print("-------------------------------------------------------")
    print(f" Se ha matriculado exitosamente en: {curso.nombre}   ")
    print("-------------------------------------------------------\n")


def mensaje_opcion_numero_invalido():
    os.system("cls")
    print("----------------------------------------")
    print("| No ha ingresado una opción válida... |")
    print("----------------------------------------\n")


def mensaje_opcion_debe_ser_numerica():
    os.system("cls")
    print("----------------------------------")
    print("| Ingrese una opción numérica... |")
    print("----------------------------------\n")


def mensaje_mail_no_registrado():
    os.system("cls")
    print("------------------------------------------------------")
    print("| Mail no registrado, debe darse de alta en alumnado |")
    print("------------------------------------------------------\n")


def mensaje_contrasenia_invalida():
    print("-----------------------------------------------")
    print("| contraseña inválida, vuelva a intentarlo... |")
    print("-----------------------------------------------\n")


def mensaje_carrera_unregistered():
    print("------------------------------")
    print("| No pertenece a esta carrera  ... |")
    print("------------------------------\n")


def mensaje_curso_unregistered():
    print("--------------------------------------------------")
    print("| No se encuentra matriculado en este curso  ... |")
    print("--------------------------------------------------\n")


def mensaje_fin_programa():
    os.system("cls")
    print("--------------------")
    print("| FIN DEL PROGRAMA |")
    print("--------------------\n")
