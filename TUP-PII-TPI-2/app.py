import os
import data
import functions

# Useful data for quick tests:

# User name: test Student, email 1 password 2
# Enrolled in career: "Tecnicatura Universitaria en programación"

# User test Professor, email 2 password 3

# Admin code is: admin123

# The program starts without courses in the system, only with the career "Tecnicatura Universitaria en programación" that has 1 enrolled student (test Student)

functions.welcome_message()

while True:
    opt = functions.main_menu()
    if opt == 1:
        active_object = functions.prompt_data_validate_credentials(opt)
        if active_object:
            while True:
                opt_student = functions.student_menu()
                os.system("clear")
                if opt_student == 1:
                    functions.prompt_enroll(active_object)
                elif opt_student == 2:
                    functions.prompt_unenroll(active_object)
                elif opt_student == 3:
                    functions.print_enrolled_courses(active_object)
                elif opt_student == 4:
                    break
    elif opt == 2:
        active_object = functions.prompt_data_validate_credentials(opt)
        if not active_object:
            register_professor = functions.register_professor()
        else:
            while True:
                opt_professor = functions.professor_menu()
                os.system("clear")
                if opt_professor == 1:
                    new_course = functions.create_new_course(active_object)
                elif opt_professor == 2:
                    functions.print_enrolled_courses(active_object)
                elif opt_professor == 3:
                    break
    elif opt == 3:
        sorted_courses = functions.sort_courses(data.course_list)
        functions.show_sorted_courses(sorted_courses)
    elif opt == 4:
        functions.end_program_message()
        break
