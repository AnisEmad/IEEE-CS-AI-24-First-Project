import methods

try:
    commands_functions = {
        1: methods.addStudent,
        2: methods.viewStudent,
        3: methods.searchStudent,
        4: methods.updateStudentDetails,
        5: methods.deleteStudentById,
        6: methods.saveToFile,
        7: methods.loadFromFile,
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

        try:
            command = int(input("Enter your command (use numbers 1 to 8): "))
        except ValueError:
            print("Invalid input. Please enter a valid command.")
            continue

        try:
            if command == 8:
                print("Exiting program")
                break
            elif command in commands_functions:
                commands_functions[command]()
            else:
                print("Invalid command, Enter numbers 1 to 8.")
        except KeyError:
            print("Command function not found.")


except KeyboardInterrupt:  # to handle user interruption
    print("\nProgram interrupted by user.")
