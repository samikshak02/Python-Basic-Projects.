def student_database():
    #empty dictionary
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                roll = input("Enter Roll No: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                # Add student using update()
                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student Added Successfully.")

            elif choice == 2:
                roll = input("Enter Roll No: ")

                # Search using get()
                record = students.get(roll)

                if record:
                    print(record)
                else:
                    print("Student Not Found.")

            elif choice == 3:
                if students:
                    for roll, details in students.items():
                        print("Roll No:", roll)
                        print(details)
                else:
                    print("No Records Found.")

            elif choice == 4:
                print("Program Ended.")
                break

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter valid input.")

student_database()







