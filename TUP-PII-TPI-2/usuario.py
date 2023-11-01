from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia
        self.__mis_cursos = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email

    @property
    def contrasenia(self):
        return self.__contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self.__contrasenia = nueva_contrasenia

    @property
    def mis_cursos(self):
        return self.__mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, nuevos_cursos):
        self.__mis_cursos = nuevos_cursos   
    
    def __str__(self):
        return self.__nombre.title()

    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        return email==self.__email and contrasenia==self.__contrasenia
        
