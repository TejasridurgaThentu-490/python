class Employee:
    def __init__(self, emp_id, emp_name, emp_hourly_wage):  # Fixed: __init__
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_hourly_wage = emp_hourly_wage

    def details(self):
        print("-----------------------------------------------")
        print("Id: ", self.emp_id)
        print("Name:", self.emp_name)
        print("Hourly wage:", self.emp_hourly_wage, "$")
        print("-----------------------------------------------")

employees = {}

def create_employee(emp_id, emp_name, emp_hourly_wage):
    # Check if the employee is already created.
    if emp_id not in employees:
        new_employee = Employee(emp_id, emp_name, emp_hourly_wage)
        employees[emp_id] = new_employee
        print("Saved", emp_name, "as a new employee")
    else:
        print("Employee", emp_id, "is already existing")

def show_employees():
    for emp_id in employees:
        employee = employees[emp_id]
        employee.details()

def update_employees(emp_id, new_name, new_hourly_wage):
    if emp_id in employees:
        employee = employees[emp_id]
        if new_name and new_hourly_wage:
            employee.emp_name = new_name
            employee.emp_hourly_wage = new_hourly_wage
            print("Employee with", emp_id, "is updated.")
        else:
            print("Invalid arguments: name and hourly wages have to be mentioned")
    else:
        print("Employee with", emp_id, "doesn't exist")

def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Successfully deleted the employee", emp_id)
    else:
        print("Employee id:", emp_id, "is not found in the registry.")

# 25 days per month, 8 hours each day, hourly wage is given.
def emp_salary(emp_id):
    if emp_id in employees:
        employee = employees[emp_id]
        salary = (25 * 8) * employee.emp_hourly_wage
        return salary
    else:
        raise Exception("Employee Not Found")

# Using the functions for managing the employees.
create_employee("Emp1", "Basha vali", 300)
create_employee("Emp2", "Ritika", 400)
create_employee("Emp3", "Radha", 350)

update_employees("Emp2", "Rithika singh", 420)
delete_employee("Emp3")
print(emp_salary("Emp1"))
show_employees()