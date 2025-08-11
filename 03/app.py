class Employee:
    def __init__(self, name, postion):
        self.name = name
        self.postion = postion
    def describe(self):
        return self.name + " pracuje jako " + self.postion

class Teacher(Employee):
    def __init__ (self, name, postion, subject):
        super().__init__(name,postion)
        self.subject = subject
    def describe(self):
        return super().describe() + " i uczy " + self.subject
    
class Policeofficer(Employee):
    def __init__ (self, name, postion, rank):
        super().__init__(name,postion)
        self.rank = rank
    def describe(self):
        return super().describe() + ", jego ranga to " + self.rank
    
employee1 = Employee("Jacek","Dyrektor")
employee2 = Teacher("Marcin", "Nauczyciel", "Historia")
employee3 = Policeofficer("Ryszard", "Śledczy", "Porucznik")
print(employee1.describe())
print(employee2.describe())
print(employee3.describe())
