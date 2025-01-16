class Arithmetic():
    a = 10
    b = 20
    
    def add(self):
        return self.a + self.b
    
    def multiply(self):
        return self.a * self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def division(self):
        return self.a / self.b
    
obj1 = Arithmetic()
obj2 = Arithmetic()
obj2.a = obj2.add()
print(obj1.add())
print(obj2.multiply())
print(obj1.subtraction())
print(obj1.division())