students = list()
id = 0
def addStudent():
    """ method used for adding a student to a temproray list of dicts """
    global id
    id += 1
    print("Enter the details of the student: ")
    name = input("Full name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    email = input("Email: ")
    address = input("Address: ")
    student = {
        "Name": name,
        "Age": age,
        "Grade": grade,
        "ID": id,
        "Email": email,
        "Address": address
        }
    students.append(student)
    print("student added sucessfully")


def viewStudent():
    """ method prints all the students in the temp database """
    for student in students:
        print("=============================================================")
        for key, value in student.items():
            print(f"{key}: {value}")
    print("=============================================================")