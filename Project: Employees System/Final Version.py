def check_input_type(type: str):
    type = type.lower()

    if type == "name":
        while True:
            lst_fname = input("Enter First Name: ").split()
            lst_lname = input("Enter Last Name: ").split()
            fname, lname = "", ""

            if len(lst_fname) > 1 or len(lst_lname) > 1 or len(lst_fname) == 0 or len(lst_lname) == 0:

                if len(lst_fname) > 1 or len(lst_fname) == 0:
                    print("Please Enter First Name Only.")

                if len(lst_lname) > 1 or len(lst_lname) == 0:
                    print("Please Enter Last Name Only.")

            else:
                fname, lname = lst_fname[0], lst_lname[0]

                if fname is not None and lname is not None and fname != "" and lname != "":
                    if fname.isalpha() and lname.isalpha():
                        return [fname.capitalize(), lname.capitalize()]
                else:
                    print("Enter Valid Name.")
                    print()

    # Age
    elif type == "age":
        while True:
            age = input("Enter Age: ").strip()
            if age is not None and age.isdigit():
                age = int(age)
                if age > 0:
                    return  age
                else:
                    print("Enter Valid Age")
                    print()
            else:
                print("Enter Valid Age.")
                print()

    else: # Salary
        while True:
            salary = input("Enter Salary: ").strip()
            if salary is not None and salary.isdigit():
                salary = int(salary)
                return salary
            else:
                print("Enter Valid Salary.")
                print()


class Employee:

    def __init__(self, fname, lname, age, salary):
        self.fname, self.lname, self.age, self.salary = fname, lname, age, salary

    def __str__(self):
        return F"Employee {self.fname} {self.lname} has age {self.age} and salary {self.salary}"

    def __repr__(self):
        return F"Employee(fname={self.fname}, lname={self.lname}, age={self.age}, salary={self.salary})"


class EmployeesManager:

    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("Please Enter Employee Data.")
        # Take Employee Data
        full_name = check_input_type("name")
        first_name = full_name[0]
        last_name = full_name[1]
        age = check_input_type("age")
        salary = check_input_type("salary")

        # Add New Employee
        self.employees.append(Employee(first_name, last_name, age, salary))
        print()

    def list_employees(self):
        if len(self.employees) == 0:
            print("There are not employees at this moment")
            return

        print("***** Employees List *****")
        for emp in self.employees:
            print(emp)

        print(" ")

    def delete_employees_by_age_range(self):
        if len(self.employees) == 0:
            print("There are not Employees")
            return

        print("Enter Age Range (From : to)")

        while True:
            age_from = check_input_type("age")
            age_to = check_input_type("age")

            if age_from <= age_to:
                break
            else:
                print("Please, Enter Valid Range.")

        ok = False
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from<=emp.age<=age_to:
                print(F"{emp.fname} {emp.lname} is Deleted from the system.")
                self.employees.pop(idx)
                ok = True

        print(" ")

        if not ok:
            print("There are not employees in this range")
            print()

    def find_employee_by_name(self):
        name = check_input_type("name")
        f_name, l_name = name[0], name[1]

        for emp in self.employees:
            if emp.fname == f_name and emp.lname == l_name:
                return emp

        print("No Employee with this Name.")
        return None

    def update_employee_salary_by_name(self):
        emp = self.find_employee_by_name()

        if emp is not None:
            salary = check_input_type("salary")
            emp.salary = salary
            print(f"Salary has Updated for {emp.fname} {emp.lname}.")
        print()

class FrontendManager:

    def __init__(self):

        self.emp_manager = EmployeesManager()

    def print_menue(self):

        options = [
            '1) Add new Employee',
            '2) List All Employees',
            '3) Delete Employees by age range',
            '4) Update Employee Salary by Name',
            '5) End The Program'
        ]

        print('\n'.join(options))
        print()
        while True:
            user_choice = input(f"Enter Your Choice from 1 to {len(options)}: ")
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice >= 1 and user_choice <= len(options):
                    return user_choice
                else:
                    print("Error: Enter value in range.")

            else:
                print("Enter Valid value.")

            print()

    def run(self):

        while True:

            user_input = self.print_menue()

            if user_input == 1:
                self.emp_manager.add_employee()

            elif user_input == 2:
                self.emp_manager.list_employees()

            elif user_input == 3:
                self.emp_manager.delete_employees_by_age_range()

            elif user_input == 4:
                self.emp_manager.update_employee_salary_by_name()

            else:
                print("Program End")
                break


if __name__ == '__main__':

    app = FrontendManager()
    app.run()

