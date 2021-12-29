class Person:
    def __init__(self,n,a):
        print("I'm from person class.")
        self.name=n
        self.age= a
        
    def show(self):
        print(f"I am {self.name} and I'm {self.age} years old")

    def setName(self,para_name):
        self.name=para_name
    
    def setAge(self, para_age):
        self.age=para_age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    

# p1=Person("Waliur","24")

# '''p1.setName("Caesar")
# p1.setAge("24")'''

# p1.show()

# p2=Person("Reem","16")

# #p2.show()

# print(p2.getName())

# print(p2.getAge())

# print(f"Hello, Dear {p2.getName()}. You are {p2.getAge()} years old.")

'''
inheritance

syntax:
class BaseClass():
    body of baseClass

class DerivedClass(BaseClass):
    body of DerivedClass
'''


class Students(Person):
    def __init__(self, n, a,f):
        super().__init__(n, a)
        print("I am from student class.")
        self.fees=f

    # overridding 
    def show(self):
        print(f"Name: {self.name} \nAge: {self.age}\nFees: {self.fees}")

    def setFees(self,para_fees):
        self.fees=para_fees


std=Students("Ayman", "16","1000")
std.setName("Anzam")
std.setAge("24")
std.setFees("2000")

std.show()
