from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__my_courses = []

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def my_courses(self):
        return self.__my_courses

    @my_courses.setter
    def my_courses(self, new_courses):
        self.__my_courses = new_courses   
    
    def __str__(self):
        return self.__first_name.title()

    def validate_credentials(self, email: str, password: str) -> bool:
        return email == self.__email and password == self.__password
