import day5

class Math():
    def __init__(self, *data):
        self.data = data
        self.sum1 = 0
        
    def add(self):
        for i in self.data:
            self.sum1 += i
        return self.sum1
    
obj = Math(1,2,3,4,54,65)
print(obj.add())

print("=========================>")

class Parent():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def printName(self):
        return f"Hello, my name is: {self.name}"
    
class Child(Parent):
    
    def __init__(self,name,age):
        self.name = "kiran"
        super().__init__(name, age)
        
        
obj = Child("Apurva", 24)
print(obj.printName())

day5.greet("apurva")
