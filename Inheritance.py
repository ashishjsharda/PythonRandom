'''
Created on Oct 13, 2019
Inheritance
@author: asharda
'''

class Parent:
    count=10
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print(self.name)
        print(self.salary)
        
class Child(Parent):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print('Name seen is ',self.name)
        Parent.display(self)
        
c=Child('Sai',2000)
c.display()
