import os
import course
import data
import student
import professor
from file import File


def prompt_data_validate_credentials(opt):
    while True:
        entered_email = input("Enter your email: ")
        entered_password = input("Enter the password: ")
        active_object = None
        if opt == 1:
            for obj in data.registry:
                if (
                    isinstance(obj, student.Student)
                    and obj.email == entered_email
                ):
                    if obj.password == entered_password:
                        validated_access = obj.validate_credentials(
                            entered_email, entered_password
                        )
                        if validated_access:
                            os.system("clear")
                            active_object = obj  # successful login!
                            access_granted_message(active_object)
                        break
                    else:
                        os.system("clear")
                        invalid_password_message()
                        return  # back to the main menu for correct email but invalid password
            else:
                os.system("clear")
                email_not_registered_message()
                return  # back to the main menu for an unregistered email

        elif opt == 2:
            for obj in data.registry:
                if (
                    isinstance(obj, professor.Professor)
                    and obj.email == entered_email
                ):
                    if obj.password == entered_password:
                        validated_access = obj.validate_credentials(
                            entered_email, entered_password
                        )
                        os.system("clear")
                        active_object = obj
                        access_granted_message(active_object)

                        break
                    else:
                        os.system("clear")
                        invalid_password_message()
                        break
            else:
                os.system("clear")
                email_not_registered_message()
                return False  # False allows entering the function to register a professor in the app
        if active_object:
            return active_object  # allows the app to continue with the professor submenu


def register_professor():
    admin_code = "admin123"
    print(
        "------------------------------------------------------"
    )
    print(
        "| Enter the administrator code to register in the system or ENTER to exit... |"
    )
    print(
        "------------------------------------------------------\n"
    )
    entered_admin_code = input("Enter the administrator code: ")
    if entered_admin_code == admin_code:
        os.system("clear")
        new_professor_name = input("Enter your name: ")
        new_professor_lastname = input("Enter your last name: ")
        new_professor_email = input("Enter your email: ")
        new_professor_password = input("Enter your password: ")
        new_professor_title = input("Enter your title: ")
        new_professor_graduation_year = input("Enter graduation year: ")

        new_professor_object = (
            professor.Professor(  # instantiate new Professor object
                new_professor_title,
                new_professor_graduation_year,
                new_professor_name,
                new_professor_lastname,
                new_professor_email,
                new_professor_password,
            )
        )
        data.registry.append(new_professor_object)
        os.system("clear")
        print("A new professor has been registered with these details:\n")
        print(f"Name: {new_professor_name}")
        print(f"Last name: {new_professor_lastname}")
        print(f"Title: {new_professor_title}")
        print(f"Graduation year: {new_professor_graduation_year}")
        print(f"Email: {new_professor_email}")
        print(f"Password: {new_professor_password}\n")
        print("Successful registration, returning to the main menu...\n")
        return True
    else:
        os.system("clear")
        print("-------------------------------------------------------------")
        print("| Incorrect administrator code, returning to the main menu... |")
        print("-------------------------------------------------------------\n")
        return False


def prompt_enroll(active_object):
    while True:
        if not data.course_list:
            os.system("clear")
            print("No courses available yet!")
            break
        else:
            sorted_courses = sorted(
                data.course_list, key=lambda course: course.code
            )  # show courses sorted by code

            index = 0
            print("-------------------------------------------------")
            for course_item in sorted_courses:
                for career in data.career_list:
                    if active_object.registration_number in [
                        student.registration_number for student in career.students
                    ]:
                        if course_item.code in [
                            course.code for course in career.courses
                        ]:
                            print(
                                f"{index + 1}- {course_item.name} - Code: {course_item.code}"
                            )
                            index += 1
            print("-------------------------------------------------\n")
        opt = input("Enter the course number you want to enroll in: ")
        if opt.isdigit():
            opt = int(opt)
            if 1 <= opt <= len(data.course_list):
                course_to_enroll = data.course_list[opt - 1]
                if (
                    course_to_enroll in active_object.my_courses
                ):  # validate that the student does not have the course in their list
                    os.system("clear")
                    enrollment_error_message()
                    return
                else:
                    enrollment_key_entered = input("Enter the enrollment key: ")
                    if (
                        enrollment_key_entered
                        == data.course_list[opt - 1].enrollment_key
                    ):
                        active_object.enroll_in_course(
                            active_object, course_to_enroll
                        )
                        os.system("clear")
                        student_found = False
                        for career in data.career_list:
                            for student in career.students:
                                if student.name == active_object.name:
                                    student_found = True  # validate that the student belongs to the career
                                    break
                        if student_found:
                            successful_enrollment_message(course_to_enroll)
                        else:
                            career_unregistered_message()
                            return
                    else:
                        invalid_password_message()
                        return
                break
            else:
                invalid_number_option_message()
                return
        else:
            must_be_numeric_option_message()
            return


def prompt_unenroll(active_object):
    while True:
        if not data.course_list:
            os.system("clear")
            print("No courses loaded in the system yet!")
            break
        elif not active_object.my_courses:
            os.system("clear")
            print("You are not enrolled in any course yet...")
            break
        else:
            index = 0
            print("------------------------------------")
            for course_item in data.course_list:
                print(f"{index + 1}- {course_item.name}")
                index += 1
            print("------------------------------------\n")
            opt = input("Enter the course number you want to unenroll from: ")
            if opt.isdigit():
                opt = int(opt)
                if 1 <= opt <= len(data.course_list):
                    course_to_unenroll = data.course_list[opt - 1]
                    if course_to_unenroll in active_object.my_courses:
                        active_object.unenroll_from_course(
                            active_object, course_to_unenroll
                        )
                        os.system("clear")
                        print("Successfully unenrolled")
                        break
                    else:
                        course_unregistered_message()
                        return
                else:
                    invalid_number_option_message()
                    return
            else:
                must_be_numeric_option_message()
                return


def print_enrolled_courses(active_object):
    while active_object.my_courses:
        print("These are all your courses:\n")
        print("-------------------")

        index = 0
        for course in active_object.my_courses:
            index += 1
            print(f"{index} - {course.name}")
            if index >= len(active_object.my_courses):
                break
        print("-------------------\n")

        selected_course = input("Enter the option corresponding to one of the courses: ")

        if selected_course.isdigit():
            selected_course = int(selected_course)
            index_b = selected_course - 1
            if 0 <= index_b < len(active_object.my_courses):
                selected_course = active_object.my_courses[index_b]
                if isinstance(active_object, student.Student):
                    print("-------------------------------------------")
                    print(f"Name: {selected_course.name}\n")
                    print("Files of the course sorted by date:")

                    sorted_files = sorted(
                        selected_course.files, key=lambda file: file.date
                    )
                    for file in sorted_files:
                        print(
                            f" - {file.name} ({file.format}) - date: {file.date}\n"
                        )
                    print("-------------------------------------------")
                    return
                elif isinstance(active_object, professor.Professor):
                    print(f"Course name: {selected_course.name}\n")
                    print(f"Enrollment key: {selected_course.enrollment_password}\n")
                    print(f"Course code: {selected_course.code}\n")
                    print(f"Number of attached files: {len(selected_course.files)}\n")

                    add_file_response = input(
                        "Do you want to add an attached file? yes/no: "
                    )
                    while add_file_response.lower() not in ["yes", "no"]:
                        print("Please enter 'yes' or 'no'.")
                        add_file_response = input(
                            "Do you want to add an attached file? (yes/no): "
                        )
                    if add_file_response == "yes":
                        file_name = input("Enter the name of the attached file: ")
                        file_format = input(
                            "Enter the format of the attached file, for example, pdf: "
                        )
                        new_file_object = File(file_name, file_format)
                        selected_course.new_file(new_file_object)
                        os.system("clear")
                        print("---------------------------------")
                        print(" File added successfully!!!  ")
                        print("---------------------------------\n")
                        break
                    else:
                        os.system("clear")
                        break
            else:
                invalid_number_option_message()
        else:
            must_be_numeric_option_message()
    if not active_object.my_courses:
        print("------------------------------")
        print("| You don't have active courses... |")
        print("------------------------------\n")


def create_new_course(active_object):
    print("Available careers:")
    for i in range(len(data.career_list)):
        print(f"{i + 1}. {data.career_list[i].name}")

    while True:
        career_number = input("Enter the number of the career you want to choose: ")
        if career_number.isnumeric():
            career_number = int(career_number)
            if 1 <= career_number <= len(data.career_list):
                chosen_career = data.career_list[career_number - 1]
                break
            else:
                print("ERROR, invalid number")
        else:
            print("Please enter ONLY NUMBERS!")
    print("---------------------------------------------------------------")
    print(f"You have selected {chosen_career.name}")
    print("---------------------------------------------------------------")
    new_course_name = input("Enter the name of the course you want to create: ")
    for existing_course in chosen_career.courses:
        if new_course_name == existing_course.name:
            print(
                "----------------------------------------------------------------------------------------------------------------------------"
            )
            print(
                f"| This course is already available in the {chosen_career.name} career, you cannot add it again|"
            )
            print(
                "----------------------------------------------------------------------------------------------------------------------------\n"
            )
            return
    else:
        new_course_key = course.Course.generate_password()
        new_course_object = course.Course(new_course_name, new_course_key)
        active_object.teach_course(
            active_object, new_course_object, chosen_career
        )
    print(
        "--------------------------------------------------------------------------------------------------------"
    )
    print(
        f" You have successfully added the course '{new_course_name}', key: '{new_course_key}', code: '{new_course_object.code}'"
    )
    print(
        "--------------------------------------------------------------------------------------------------------\n"
    )
    return


def sort_courses(course_list):
    sorted_courses_list = sorted(course_list, key=lambda x: x.name)
    return sorted_courses_list


def show_sorted_courses(sorted_course_list):
    if not sorted_course_list:
        os.system("clear")
        print("-------------------------------------------")
        print("| There are no courses loaded in the system... |")
        print("-------------------------------------------\n")
    else:
        os.system("clear")
        for career in data.career_list:
            for course in sorted_course_list:
                for career_course in career.courses:
                    if career_course.name == course.name:
                        print(f"Course name: {course.name} Career: {career.name}")
        print("------------------------------\n")


def main_menu():
    print("-------------------------------")
    print("|1 - Log in as a student      |")
    print("|2 - Log in as a professor    |")
    print("|3 - View courses             |")
    print("|4 - Exit                     |")
    print("-------------------------------\n")

    opt = input("Enter the menu option: ")
    if opt.isdigit():
        opt = int(opt)
        if 1 <= opt <= 4:
            return opt
        else:
            invalid_number_option_message()
    else:
        must_be_numeric_option_message()


def welcome_message():
    print("▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
    print("| | | | | | | | | | | | | | | |")

    print(" Please enlarge the terminal")
    print("    to better visualize")
    print("        the program      ")
    print("-------------------------------")
    print("|         WELCOME!            |")
    print("-------------------------------\n")


def access_granted_message(active_object):
    print("------------------------------------------------")
    print(f"Access granted! Welcome: {active_object.first_name}")
    print("------------------------------------------------\n")


def student_menu():
    print("----------------------------------------")
    print("|1 - Enroll in a course               |")
    print("|2 - Unenroll from a course           |")
    print("|3 - View course                      |")
    print("|4 - Back to main menu                |")
    print("----------------------------------------\n")

    opt = input("Enter the menu option: ")
    if opt.isdigit():
        opt = int(opt)
        if 1 <= opt <= 4:
            return opt
        else:
            invalid_number_option_message()
    else:
        must_be_numeric_option_message()


def professor_menu():
    while True:
        print("----------------------------------------")
        print("|1 - Teach a course                   |")
        print("|2 - View course                      |")
        print("|3 - Back to main menu                |")
        print("----------------------------------------\n")

        opt = input("Enter the menu option: ")
        if opt.isdigit():
            opt = int(opt)
            if 1 <= opt <= 3:
                return opt
            else:
                invalid_number_option_message()
        else:
            must_be_numeric_option_message()


def enrollment_error_message():
    print("----------------------------------------------")
    print("| You are already enrolled in this course... |")
    print("----------------------------------------------\n")


def successful_enrollment_message(course):
    print("-------------------------------------------------------")
    print(f" Successfully enrolled in: {course.name}   ")
    print("-------------------------------------------------------\n")


def invalid_number_option_message():
    os.system("clear")
    print("------------------------------------------")
    print("| You have not entered a valid option... |")
    print("------------------------------------------\n")


def must_be_numeric_option_message():
    os.system("clear")
    print("-----------------------------")
    print("| Enter a numeric option... |")
    print("-----------------------------\n")


def email_not_registered_message():
    os.system("clear")
    print("-------------------------------------------------------")
    print("| Email not registered, you must register in student  |")
    print("-------------------------------------------------------\n")


def invalid_password_message():
    print("-----------------------------------------")
    print("| Invalid password, please try again... |")
    print("-----------------------------------------\n")


def career_unregistered_message():
    print("-----------------------------------------")
    print("| You do not belong to this career  ... |")
    print("-----------------------------------------\n")


def course_unregistered_message():
    print("--------------------------------------------------")
    print("| You are not enrolled in this course  ...       |")
    print("--------------------------------------------------\n")


def end_program_message():
    os.system("clear")
    print("------------------")
    print("| END OF PROGRAM |")
    print("------------------\n")
