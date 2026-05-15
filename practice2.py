def f_to_c(f):
    c = (f-32)*5/9
    return c

f = int(input("Enter tempreature in fahrenheit: "))
c = f_to_c(f)
print("Temperature in Celsius:", c)












##########deleted# 

class Student:
    name = "Anamika"
    age = 19 
    marks = 100
    def info(self):
        print(f"{self.name} is a student of class 12th and scored {self.marks} marks")

s = Student()
print(s.name)
s.info()


class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
    def greet(self):
        print(f"{self.name} is a {self.occ}")

p = Person("Anamika", "software developer")
p.greet()