class Employee:
    def __init__(self, name, last_name, monthly_salary):
        self.name = name
        self.last_name = last_name
        self.__monthly_salary = monthly_salary

    def getFullName(self):
        return self.name+ " "+ self.last_name

    def annualSalary(self):
        return "High" if self.__monthly_salary*12 > 100 else "Low"
    
e1 = Employee("Emil", "Alzarif", 20)
e2 = Employee("Kristina", "Sahakyan", 8)    

print(e1.getFullName())
print(e1.annualSalary())

print(e2.getFullName())
print(e2.annualSalary())