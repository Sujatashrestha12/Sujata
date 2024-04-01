#inheritamce>- the process of inheriting the properties of the parent class.

class Person:
    def person_info(self,name,age):
        print("Inside Person Class")
        self.name = name
        print("Name: ", name, "Age: ", age)

class Company:
    def company_info(self, company_name, location):
        print("Inside Company Class")
        self.company_name = company_name
        print("Company name: ", company_name, "location: ", location)

class Employee(Person, Company):
    def employee_info(self, salary, skills):
        super().person_info('Binod', 20)
        print("Inside Employee class")
        print("Salary: ", salary, "Skill: ", skills)

emp = Employee()
emp.person_info('Jessi', 28)
emp.employee_info(1200,"Machine")
