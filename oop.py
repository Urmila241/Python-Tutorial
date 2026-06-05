# OOPS
# CLASS IS A BLUEPRINT FOR CREATING OBJECTS
# syntx of class
# class Classname:
    # constructor
    # variable
    # method
# object=Classname()
# CONSTRUCTOR=all classes have a function called __init__() which is always executed when 
# the class is bieng initiated
# "The Self parameter is a reference to the current instance of a class, and is used to access
#  variables that belong to the class"
# Attributes=data or variables
class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("Adding new student in database")
s1=Student("karan",97)
print(s1.name)
print(s1.marks)
# class Book:
#     def __init__(self,title,author,pages):
#         # print(title,author)
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def read(self,page):
#         print(f"I have read {page} pages of this book")
# book1=Book("Daughter of east","Benazir Bhuto",442)
# book1.read(50)
# print(book1.author)

class Classroom:
    def __init__(self,furniture,students,laptops):
        print(furniture,students)
cr1=Classroom("chair table","female","lenovo")
