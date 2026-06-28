class Employee:
    # Initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    # Display employee details
    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print()

# Create an empty dictionary
employees = {}
# Add 3 employees
for i in range(3):
    print("Employee Information")
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    print("-------------------------------")
    emp = Employee(emp_id, name, department, salary)

    # Store object in dictionary
    employees[emp_id] = emp
# Display all employees
print("\nEmployee Details")
for emp in employees.values():
    emp.show_details()

