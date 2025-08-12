class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def describe(self):
        return self.name + " pracuje jako " + self.position

class Teacher(Employee):
    def __init__ (self, name, postion, subject):
        super().__init__(name,postion)
        self.subject = subject
    def describe(self):
        return super().describe() + " i uczy " + self.subject
    
class PoliceOfficer(Employee):
    def __init__ (self, name, postion, rank):
        super().__init__(name,postion)
        self.rank = rank
    def describe(self):
        return super().describe() + ", jego ranga to " + self.rank
    
employee_1 = Employee("Jacek","Dyrektor")
employee_2 = Teacher("Marcin", "Nauczyciel", "Historia")
employee_3 = PoliceOfficer("Ryszard", "Śledczy", "Porucznik")
print(employee_1.describe())
print(employee_2.describe())
print(employee_3.describe())
