class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print("Czesc, mam na imie",self.name, ",mam",self.age, "lat i mieszkam w",self.city)

person_0 = Person("Maciej",17,"Sopot")
person_1 = Person("Kasia",23,"Gdynia")
person_2 = Person("Krystian",37,"Gdansk")

person_0.introduce()
person_1.introduce()
person_2.introduce()