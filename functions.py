# Modules Used

from prettytable import PrettyTable


# Color Functions

def red_text(text):
    return f"\033[91m{text}\033[0m"


def green_text(text):
    return f"\033[92m{text}\033[0m"


def yellow_text(text):
    return f"\033[93m{text}\033[0m"


def blue_text(text):
    return f"\033[94m{text}\033[0m"


def orange_text(text):
    return f"\033[38;5;208m{text}\033[0m"


# Input Function

def input_data():
    data_append = open("student.txt", 'a')
    try:
        n_students = int(input(blue_text('\nEnter number of students: ')))
        print(orange_text('\nFill in all the details! \n'))
        last_admission_number = get_last_admission_number()
        for _ in range(n_students):
            name = input(blue_text('Enter Name: '))
            clss = input(blue_text('Enter Class: '))
            section = input(blue_text('Enter Section: '))
            admission_number = str(last_admission_number + 1).zfill(4)
            print(f"\n{green_text('Admission Number: ')}{admission_number}\n")
            data_append.write(f"{name},{clss},{section},{admission_number}\n")
            last_admission_number += 1
        data_append.close()
        print(green_text('Record saved successfully!'))
    except ValueError:
        print(red_text("\nPlease input only integer!"))
        input_data()


# Function to fetch last admission number

def get_last_admission_number():
    try:
        with open("student.txt", "r") as f:
            lines = f.readlines()
        if lines:
            last_line = lines[-1]
            last_admission_number = int(last_line.strip().split(',')[3])
            return last_admission_number
    except FileNotFoundError:
        pass
    return 0


# Output Function

def output_data():
    try:
        data_read = open("student.txt")
        myTable = PrettyTable(["Student Name", "Class", "Section", "Admn. No."])
        for line in data_read:
            x = line.strip().split(',')
            myTable.add_row(x)
        print(f"\n{myTable}")
        data_read.close()
    except FileNotFoundError:
        print(f"\n{red_text('NO RECORDS PRESENT. Add records to get started.')}")


# Deleting Function

def del_data():
    try:
        with open("student.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print(f"\n{red_text('NO RECORDS PRESENT. Add records to get started.')}")
            return
        name = input(blue_text('\nEnter Name of the Student: '))
        admn_no = input(blue_text('Enter Admn. No.: '))
        found = False
        updated_lines = []
        for line in lines:
            l = line.strip('\n').split(',')
            if l[0] == name and l[-1] == admn_no:
                found = True
                confirmation = input(red_text(f"\nConfirm deletion of {l[0]} [Y/N]: ")).lower()
                if confirmation == 'y':
                    print(green_text('\nStudent information deleted successfully!'))
                else:
                    print(red_text('\nDELETION ABORTED.'))
                    updated_lines.append(line)
            else:
                updated_lines.append(line)
        if not found:
            print(red_text('\nSTUDENT NOT FOUND. No records deleted.'))
        if found:
            with open("student.txt", "w") as f:
                f.writelines(updated_lines)
    except FileNotFoundError:
        print(f"\n{red_text('NO RECORDS PRESENT. Add records to get started.')}")


# Searching Functions

def search_by_admission_number(data_read):
    admission_number = input(blue_text('\nEnter admission number of student to search for: '))
    myTable = PrettyTable(["Student Name", "Class", "Section", "Admission No."])
    for line in data_read:
        student_data = line.strip().split(',')
        if student_data[3] == admission_number:
            myTable.add_row(student_data)
            print(f"\n{myTable}")
            break
    else:
        print(red_text("\nNO RECORDS FOUND!"))


def search_by_name_and_class(data_read):
    name = input(blue_text('\nEnter name of student to search for: '))
    clss = input(blue_text('Enter his/her class: '))
    myTable = PrettyTable(["Student Name", "Class", "Section", "Admission No."])
    for line in data_read:
        student_data = line.strip().split(',')
        if student_data[0] == name and student_data[1] == clss:
            myTable.add_row(student_data)
            print(f"\n{myTable}")
            break
    else:
        print(red_text("\nNO RECORDS FOUND!"))


def search_data():
    data_read = open("student.txt")
    print(f"\n"
          f"{yellow_text('Which method do you want to use?')}\n"
          f"\nBy Admission Number: {yellow_text('1')}\n"
          f"By Name and Class: {yellow_text('2')}\n"
          f"Exit: {yellow_text('E')}"
          f"")
    n = input(blue_text('\nEnter method: '))
    if n == '1':
        search_by_admission_number(data_read)
        search_data()
    elif n == '2':
        search_by_name_and_class(data_read)
        search_data()
    elif n.upper() == 'E':
        data_read.close()
    else:
        print(red_text('\nENTER A VALID OPTION!'))
        search_data()
