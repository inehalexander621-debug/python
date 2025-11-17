# Build a Person class with name and age.
#  Inherit it in a Student class with an added course attribute.
#  Create and display two student objects.


# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Child class
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print("--------------")

# Creating two student objects
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("John", 22, "Software Engineering")

# Display the students
student1.display()
student2.display()