class Employee:
    def name(self):
        print("Employee name Sidra")

class Company(Employee):
    def cname(self):
        print("Company Name Wipro")

a=Company()
a.cname()
a.name()
