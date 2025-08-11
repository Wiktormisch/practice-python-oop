class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return "'" + self.title + "' - " + self.author + "(" + self.year + ")"
    
book1 = Book("Imopeksis", "Tomasz Wilczewski", "2020")
book2 = Book("1984", "George Orwell", "1949")
book3 = Book("Michael Jordan Zycie", "Roland Lazenby", "2014")


print(book1)
print(book2)
print(book3)