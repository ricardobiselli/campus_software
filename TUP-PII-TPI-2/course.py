import string
import random
import file


class Course:
    __next_code = 10

    def __init__(self, name: str, enrollment_password: str):
        self.__name = name
        self.__enrollment_password = enrollment_password
        self.__code = Course.__get_course_code()
        self.__files = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def enrollment_password(self) -> str:
        return self.__enrollment_password

    @enrollment_password.setter
    def enrollment_password(self, enrollment_password: str):
        self.__enrollment_password = enrollment_password

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def files(self) -> list:
        return self.__files

    def new_file(self, new_file: file.File):
        self.__files.append(new_file)

    @classmethod
    def __get_course_code(cls) -> int:
        cls.__next_code += 1
        return cls.__next_code

    @classmethod
    def generate_password(cls):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(8))
        return password

    def __str__(self):
        return f"Name: {self.__name} - Files {len(self.__files)}"
