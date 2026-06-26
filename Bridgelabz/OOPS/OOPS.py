# class student:
#     name = "Karan"

# S1 = student() 
# print(S1.name) 

# class car:
#     color = "blue"
#     brand = "BMW"

# C = car()
# print("The color of the car is:", C.color)
# print("The brand of the car is:", C.brand) 

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

# S1 = student("Karan", 20) 
# print("The name of the student is:", S1.name)
# print("The age of the student is:", S1.age) 

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def avg(self):
#         return sum(self.marks)/len(self.marks)

# S1 = student("Vanitha", [20, 40, 90])
# print("The name of the student is:", S1.name)
# print("The average marks of the student is:", S1.avg()) 

# class student:
#     @staticmethod
#     def greet():
#         print("Hello, welcome to the class!") 

# student.greet() 

# class car:
#     def start(self):
#         print("The car has started.") 

# C = car()
# C.start() 

# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.", amount, "has been debited from your account.") 
#         print("Total balance is:", self.get_balance())  
    
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.", amount, "has been credited to your account.") 
#         print("Total balance is:", self.get_balance()) 
    
#     def get_balance(self):
#         return self.balance

# A1 = Account(1000, "1234567890")
# A1.debit(100) 
# A1.credit(20000) 

#Inheritance
#Single Inheritance
# class Parent:
#     def show(self):
#         print("This is the parent class.")

# class Child(Parent):
#     def display(self):
#         print("This is the child class.") 

# C = Child()
# C.show()
# C.display()

#Multiple Inheritance
# class father:
#     def show_father(self):
#         print("This is the father class.")

# class mother:
#     def show_mother(self):
#         print("This is the mother class.")

# class child(father, mother):
#     def show_child(self):
#         print("This is the child class.") 

# C = child()
# C.show_father()
# C.show_mother()
# C.show_child() 

#Multilevel Inheritance
# class grandparent:
#     def show_grandparent(self):
#         print("This is the grandparent class.")

# class parent(grandparent):
#     def show_parent(self):
#         print("This is the parent class.") 

# class child(parent):
#     def show_child(self):
#         print("This is the child class.") 

# C = child()
# C.show_grandparent()
# C.show_parent()
# C.show_child() 

#Hierarchical Inheritance
# class Parent:
#     def show_parent(self):
#         print("This is the parent class.")

# class Child1(Parent):
#     def show_child1(self):
#         print("This is the child1 class.")

# class Child2(Parent):
#     def show_child2(self):
#         print("This is the child2 class.")

# C1 = Child1()
# C2 = Child2()
# C1.show_parent()
# C1.show_child1() 
# C2.show_parent()
# C2.show_child2() 

#Hybrid Inheritance
# class A:
#     def show_A(self):
#         print("This is class A.")

# class B(A):
#     def show_B(self):
#         print("This is class B.")

# class C(A):
#     def show_C(self):
#         print("This is class C.")

# class D(B, C):
#     def show_D(self):
#         print("This is class D.")

# D1 = D()
# D1.show_A()
# D1.show_B()
# D1.show_C() 
# D1.show_D() 

#Python scopes and namespaces
# x = 10
# def func():
#     y = 20
#     print("Inside the function, x =", x, "and y =", y) 

# func()
# print("Outside the function, x =", x) 

#Instance objects
# class Person:
#     def __init__(self, name):
#         self.name = name

# p1 = Person("Anand")
# p2 = Person("Rahul")

# print(p1.name)
# print(p2.name) 

#Method Objects
# class example:
#     def instance_method(self):
#         print("This is an instance method.")
    
#     @classmethod
#     def class_method(cls):
#         print("This is a class method.") 
    
#     @staticmethod
#     def static_method():
#         print("This is a static method.") 

# E = example()
# E.instance_method()
# E.class_method()
# E.static_method() 

#Class vs Instance Variables
# class student:
#     school = "SRM"

#     def __init__(self,name):
#         self.name = name

# S1 = student("Karan")
# S2 = student("Vanitha") 
# print("Student 1 name:", S1.name)
# print("Student 2 name:", S2.name) 
# print("Student 1 school:", S1.school)
# print("Student 2 school:", S2.school) 

#Private Variables
# class bank:
#     def __init__(self, balance):
#         self.__balance = balance 

#     def get_balance(self):
#         return self.__balance

# B = bank(1000)
# print("The balance in the bank account is:", B.get_balance()) 

#Iterators
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# it = iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) 
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) 

#Generators
# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for i in gen():
#     print(i) 

#Decorators
# def decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello, world!") 
# say_hello() 

#Pydantic
# from pydantic import BaseModel
# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# user = User(name="Anand", age=25, email="anand@example.com")
# print(user) 

#SOLID Principles
# class report:
#     def generate(self):
#         print("Generating report")
    
# class printer:
#     def print(self):
#         print("Printing report")

# R = report()
# P = printer()
# R.generate()
# P.print() 

#DRY Principle
# def greet():
#     print("Hello, welcome to the class!") 
# greet()   

#YAGNI Principle
# class simple:
#     def show(self):
#         print("This is a simple class.") 

# S = simple()
# S.show() 