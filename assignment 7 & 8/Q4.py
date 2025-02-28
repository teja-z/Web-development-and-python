
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            combined_salary = self.salary + other.salary
            combined_name = self.name + " & " + other.name
            return Employee(combined_name, combined_salary)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            salary_difference = self.salary - other.salary
            return salary_difference
        return NotImplemented

    def display(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

def main():
    num_employees = int(input("Enter the number of employees: "))
    employees = []

    for i in range(num_employees):
        print(f"\nEnter details for Employee {i+1}:")
        name = input("Enter the name: ")
        salary = float(input(f"Enter the salary of {name}: "))
        emp = Employee(name, salary)
        employees.append(emp)

    print("\nEmployee Details:")
    for emp in employees:
        emp.display()

    if num_employees >= 2:
        for i in range(num_employees):
            for j in range(i+1, num_employees):
                combined_employee = employees[i] + employees[j]
                print(f"\nCombined Employee ({employees[i].name} & {employees[j].name}):")
                combined_employee.display()

                salary_diff = employees[i] - employees[j]
                print(f"Salary Difference between {employees[i].name} and {employees[j].name}: {salary_diff}")
    else:
        print("\nNot enough employees to combine or compare salaries.")

if __name__ == "__main__":
    main()
