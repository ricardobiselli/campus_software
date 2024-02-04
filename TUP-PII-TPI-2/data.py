from professor import Professor
from student import *
from career import *

registry = [
    Student(53013, 2023, "Ricardo", "Biselli",
            "ricardobiselli@gmail.com", "131313"),
    Student(
        11111, 2023, "test user 1", "test user lastname", "1", "2"
    ),  # email: 1 password: 2 for quick testing
    Professor(
        "full stack developer",
        2010,
        "Mercedes",
        "Valoni",
        "mercedes@gmail.com",
        "mercedes123",
    ),
    Professor(
        "sysadmin",
        2011,
        "test user 2",
        "perez",  # email: 2 password: 3 for quick testing
        "2",
        "3",
    ),
]

# course_1 = Course("Programming 1", "prog1")
# course_2 = Course("Programming 2", "prog2")
# course_3 = Course("English 1", "ing1")
# course_4 = Course("English 2", "ing2")
# course_5 = Course("Laboratory 1", "lab1")
# course_6 = Course("Laboratory 2", "lab2")

course_list = []

career1 = Career("University Technician in Programming", 2)
# career2 = Career("Another test career", 5)

career_list = []

career_list.append(career1)
# career_list.append(career2)

# career1.add_course(course_list[0])
# career1.add_course(course_list[1])
# career1.add_course(course_list[2])
# career1.add_course(course_list[3])
# career1.add_course(course_list[4])
# career1.add_course(course_list[5])

# career2.add_course(course_list[1])

career1.add_student(registry[1])
