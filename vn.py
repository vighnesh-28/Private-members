class Employee:
    def __init__(self, name, salary):
        self.name = name    # public
        self.__salary = salary  # private

    def show_salary(self):
        print("salary:", self.__salary)


emp = Employee("Robert",600000)
print(emp.name)   # public accessible
emp.show_salary()  # Accessing private correctly
# print(emp.__salary)  # Error: Not accessible directly
