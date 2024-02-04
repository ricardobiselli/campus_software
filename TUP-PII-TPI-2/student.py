from user import *


class Student(User):
    def __init__(
        self,
        student_id: int,
        enrollment_year: int,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ):
        super().__init__(first_name, last_name, email, password)
        self.__student_id = student_id
        self.__enrollment_year = enrollment_year
        self.__my_courses = []

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def enrollment_year(self):
        return self.__enrollment_year

    @enrollment_year.setter
    def enrollment_year(self, enrollment_year):
        self.__enrollment_year = enrollment_year

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def enroll_in_course(self, active_object, course_to_enroll):
        active_object.my_courses.append(course_to_enroll)

    def disenroll_course(self, active_object, course_to_disenroll):
        active_object.my_courses.remove(course_to_disenroll)
