from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        self._mis_cursos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self._contrasenia = nueva_contrasenia

    @property
    def mis_cursos(self):
        return self._mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, nuevos_cursos):
        self._mis_cursos = nuevos_cursos   
    
    def __str__(self):
        return self._nombre.title()

    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        return email==self._email and contrasenia==self._contrasenia
        
