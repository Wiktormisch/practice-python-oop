class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        return self.name + " wydaje dzwiek"

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        return self.name + " szczeka: hau hau!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        return self.name + " miauczy: miau miau!"
    
class Bird(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        return self.name + " śpiewa: ćwir ćwir!"


animals_list = [Dog("Mia"), Dog("Fado"), Cat("Frania"), Cat("Jasia"), Dog("Pikus"), Bird("Tweety"), Bird("Wrobelek")]

for animal in animals_list:
    print(animal.make_sound())