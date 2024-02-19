import methods
import file_methods

try:
    commands_functions = {
        1: methods.addStudent,
        2: methods.viewStudent,
        3: methods.searchStudent,
        4: methods.updateStudentDetails,
        5: methods.deleteStudentById,
        6: file_methods.saveToFile,
        7: file_methods.loadFromFile
    }

    print("*" * 43)
    print(f"    Student Database Management System")
    print("*" * 43)

    while True:
        print("\n1. Add Student"
              "\n2. View Students"
              "\n3. Search Student"
              "\n4. Update student details"
              "\n5. Delete student"
              "\n6. Save to File"
              "\n7. Load from File"
              "\n8. Exit")

        command = int(input("Enter your command: "))

        if command in commands_functions.keys():
            commands_functions[command]()

        elif command == 8:
            print("Exiting program")
            break
        else:
            print("Invalid command.")


except ValueError as e:
    print(f"\nError: {e}")
except IndexError as e:
    print(f"\nError: {e}")
except TypeError as e:
    print(f"\nError: {e}")
except KeyError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:  # to handle user interruption
    print("\nProgram interrupted by user.")
