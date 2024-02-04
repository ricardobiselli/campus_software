from user import *
import data


class Professor(User):
    def __init__(self, title: str, graduation_year: int, first_name: str, last_name: str, email: str, password: str):
        self.__title = title
        self.__graduation_year = graduation_year
        super().__init__(first_name, last_name, email, password)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def graduation_year(self):
        return self.__graduation_year

    @graduation_year.setter
    def graduation_year(self, value):
        self.__graduation_year = value

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def teach_course(self, active_object, new_course_object, major):
        # add the course to the professor's list of courses
        active_object.my_courses.append(new_course_object)
        # add the course to the general list of courses
        data.course_list.append(new_course_object)
        # add the course to the major
        major.courses.append(new_course_object)
