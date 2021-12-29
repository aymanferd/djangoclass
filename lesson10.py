'''
class

A class is a blueprint for the object. 
An object has two characteristics. 
1. Attributes 
2.behavior 


syntax:
class <ClassName>(object):
    <snippets>

making an instance(object) from a class.
ObjectName=ClassName(arguments)


'''

class MyClass(object):
    '''this is a sample class'''
    a=10
    def myfunc(self):
        print("hello")

    
'''creating class object'''

obj1=MyClass()

print(obj1.a)

obj1.myfunc()

print(MyClass.__doc__)

