class Student:
    # Initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Add marks
    def add_mark(self, mark):
        try:
            mark = float(mark)

            if mark < 0 or mark > 100:
                print("Invalid marks")
            else:
                self.marks_list.append(mark)

        except ValueError:
            print("Please enter a valid number.")

    # Calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Display student details
    def display_info(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())

name = input("Enter Name: ")
roll_no = input("Enter Roll No: ")

# Create object
student = Student(name, roll_no)

# Take 5 marks
for i in range(5):
    mark = input("Enter mark: ")
    student.add_mark(mark)

# Display information
student.display_info()

