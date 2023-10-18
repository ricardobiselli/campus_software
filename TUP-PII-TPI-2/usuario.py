from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self):
        return self._nombre.title()

    
    def validar_credenciales(self, tipo_usuario, email: str, contrasenia: str) -> bool:
        return email==self._email and contrasenia==self._contrasenia
        email_encontrado = False
        for user in tipo_usuario:
            if email == user["email"]:
                email_encontrado = True
                if contrasenia == user["contraseña"]:
                    print("YES! validacion mètodo estático")  # temporal
                    return True
                else:
                    print("Contraseña incorrecta")
                    return False

        if not email_encontrado:
            print("Mail no registrado, debe darse de alta en alumnado")
            return False
