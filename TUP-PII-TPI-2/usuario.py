from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        self._mis_cursos = []

    def __str__(self):
        return self._nombre.title()

    
    def validar_credenciales(self, email: str, contrasenia: str) -> bool:
        return email==self._email and contrasenia==self._contrasenia
        
