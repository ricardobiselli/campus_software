class Career:
    def __init__(self, name: str, duration_years: int) -> None:
        self.__name = name
        self.__duration_years = duration_years
        self.__courses = []
        self.__students = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration_years(self):
        return self.__duration_years

    @duration_years.setter
    def duration_years(self, duration_years):
        self.__duration_years = duration_years

    def __str__(self):
        pass

    def get_course_count(self) -> int:
        return len(self.__courses)

    @property
    def courses(self):
        return self.__courses

    def add_course(self, course):
        self.__courses.append(course)

    @property
    def students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)
