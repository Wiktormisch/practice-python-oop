class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.year})"
    
book_1 = Book("Imopeksis", "Tomasz Wilczewski", "2020")
book_2 = Book("1984", "George Orwell", "1949")
book_3 = Book("Michael Jordan Zycie", "Roland Lazenby", "2014")


print(book_1)
print(book_2)
print(book_3)