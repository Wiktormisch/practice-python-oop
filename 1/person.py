class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print("Czesc, mam na imie",self.name, ",mam",self.age, "lat i mieszkam w",self.city)

person0 = person("Maciej",17,"Sopot")
person1 = person("Kasia",23,"Gdynia")
person2 = person("Krystian",37,"Gdansk")

person0.introduce()
person1.introduce()
person2.introduce()