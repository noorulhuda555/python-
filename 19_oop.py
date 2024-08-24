class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

# Creating an instance of the Book class
#my_book = Book("1984", "George Orwell", 1949)

# Printing the instance to see the output of the __str__ method
#print(my_book)

class Course:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor

    def __str__(self):
        return f"'{self.name}' by {self.instructor}"


def main():
    c1=Course("english", "bob")
    c2=Course("maths", "patrick")
    c3=Course("science", "alice")

    print(c1)
    print(c2)
    print(c3)

main()

"""When you call print(c1):

Python tries to convert the c1 object (which is an instance of the Course class) into a string.
To do this, it checks if the Course class has a __str__ method defined.
Since you have defined a __str__ method in the Course class, Python calls this method.
The __str__ method returns the formatted string "'english' by bob", which is then printed by the print() function.
"""
