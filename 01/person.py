class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print("Czesc, mam na imie",self.name, ",mam",self.age, "lat i mieszkam w",self.city)

person0 = Person("Maciej",17,"Sopot")
person1 = Person("Kasia",23,"Gdynia")
person2 = Person("Krystian",37,"Gdansk")

person0.introduce()
person1.introduce()
person2.introduce()