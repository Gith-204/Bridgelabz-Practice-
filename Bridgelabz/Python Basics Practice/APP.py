#Program 1: To print hello world
print("Hello world") 

#Program 1.1: Add two numbers with print format
a = 10 
b = 20
print("The sum of {} and {} is {}".format(a,b,a+b)) 

#Program 1.2: Adding two numbers measuring time
import time
start = time.time()
a = 100
b = 200
result = a + b
end = time.time() 
print(f"The result of adding {a} and {b} is {result}") 
print(f"---{(end-start)*1000000} micro seconds---") 
start = time.time() 
a = 100
b = 200
result = a+b
end = time.time() 
print(f"The Result of adding {a} and {b} is {result}") 
print(f"--- {(end - start)*1000000} micro seconds ---") 

#Program 2: Descriptive Variable names
z = 30
print("The value of z is",z)
print("Final Score is",z) 

#Program 3: Define function
def calculate_sum(a,b):
    z = a+b
    print("The value of z is",z)
    return z
result = calculate_sum(10,20) 
print("The final score is",result) 

#Program 4.1: Proper Function usage
def add(a,b):
    return a+b
result = add(10,20)
print("The final score is",result) 

#Program 4.2: Function Parameter Type Annotation
def add(a: int, b: int) -> int:
    total_sum = a+b
    bonus_points = 0
    print("Datatype of total_sum is", type(total_sum), "and bonus_points is", type(bonus_points)) 
    return total_sum + bonus_points
result = add(18,12) 
print("The final score is",result) 

#Program 5.1: Hard coding values
radius = 2
pi = 3.14
area = pi * radius * radius
print("Area of a circle with radius =", radius, "is", area) 

#Program 5.2: Remove hard coding 
total_sum = input("Enter value for total sum: ")
bonus_points = input("Enter value for bonus points: ") 
print("Datatype of total_sum is", type(total_sum), "and bonus_points is", type(bonus_points)) 
final_score = total_sum + bonus_points
print("The final score is", final_score)  

#Program 5.3: Handling type conversion
total_sum = int(input("Enter value for total sum: "))
bonus_points = int(input("Enter value for bonus points: "))
print("Datatype of total_sum is", type(total_sum), "and bonus_points is", type(bonus_points)) 
final_score = total_sum + bonus_points
print("The final score is", final_score) 

#Program 6.1: Handling user error
try:
    total_sum = int(input("Enter value for total sum: "))
    print("You entered", total_sum) 
except ValueError:
    print("Invalid input. Please enter a valid integer value for total sum.")

#Program 6.2: Handling exact user error
try:
    total_sum = int(input("Enter value for total sum: "))
    bonus_points = int(input("Enter value for bonus points: "))
    print("Datatype of total_sum is", type(total_sum), "and bonus_points is", type(bonus_points))
    final_score = total_sum + bonus_points 
    print("The final score is", final_score) 
except ValueError:
    print("Invalid input. Please enter valid integer values for total sum and bonus points.")  

