#Encapsulation is the concept of 

class Employee:

    def __init__(self, name, project,salary):
        self.name = name
        self._project = project
        self.__salary = salary

    def show(self):
        print("Name: ",self.name)

emp = Employee("Madhav","Xavier",1000)
emp.show()
print(emp.name)
print(emp._project)
print(emp._Employee__salary)