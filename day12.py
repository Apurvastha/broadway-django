#Multi Level Inheritance

class User():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Person(User): 
    def printName(self):
        return f"Hello, my name is: {self.name}"
    
class Child(Person):
    def printDetails(self):
        return f"Hello, my name is: {self.name}, I am {self.age} years old."
    
child = Child("Apurva", 24)
print(child.printName())
print(child.printDetails())

print("===================================================================================>")

class Student():
    def __init__(self, name, **marks):
        self.name = name
        self.marks = marks
        
class Marks(Student):
    def percentage(self):
        total = 0
        for i in self.marks.values():
            total += i
        return total/len(self.marks)
    
    def grade(self):
        if self.percentage() >= 80:
            return "A"
        elif self.percentage() >= 60:
            return "B"
        elif self.percentage() >= 40:
            return "C"
        else:
            return "F"
        
        
class Student_profile(Marks):     
    def printDetails(self):
        details = f"Name: {self.name}\n"
        for subject, mark in self.marks.items():
            details += f"  {subject}: {mark}\n"
        details += f"Total Percentage: {self.percentage():.2f}%\n"
        details += f"Grade: {self.grade()}"
        return details
    

def get_input():
    name = input("Enter your name: ")
    marks={}
    for _ in range(3):
        sub = input("Enter subject name: ")
        mark = int(input("Enter marks: "))
        marks[sub] = mark
        print("=====================================")
        
    return name, marks

name, marks = get_input()
student = Student_profile(name, **marks)
print(student.printDetails())


    
    
    