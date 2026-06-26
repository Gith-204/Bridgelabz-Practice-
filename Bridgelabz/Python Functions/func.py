#1. Define a function called greet_function that prints "Hello" to the console. 
# def greet_function():
#     print(f"Hello")
# greet_function() 

#2. Define a function called greet_function that prints "Hello Alice" to the console.
# def greet_function(name):
#     print(f"Hello {name}")
# greet_function("Alice") 

#3. Define a function called greet_function that takes a name as an argument and prints multiple greetings.
def greet_friend(name):
    print(f"Hello {name}! How are you?") 

greet_friend("Alice")
greet_friend("Bob") 

#4. Define a function called greet_friend and validate user input.
# def greet_friend(name):
#     if name.isalpha():
#         print(f"hello {name}! How are you?")
#     else:
#         print(f"Please enter a valid name with alphabetic characters only") 

# name = input("Enter your name: ") 
# greet_friend(name) 

#5. Car loan payment 
# def calculate_car_loan_payment(P,Y,R):
#     r = R / 100 / 12
#     n = Y * 12
#     monthly_payment = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1) 
#     return round(monthly_payment, 2) 

# principal_amount = float(input("Enter the principal amount in rupees: "))
# years_to_pay_off = float(input("Enter the duration to pay off the loan in years: "))
# annual_interest_rate = float(input("Enter the annual interest rate (in percentage): ")) 

# monthly_payment = calculate_car_loan_payment(principal_amount, years_to_pay_off, annual_interest_rate)
# print(f"The monthly payment for the car loan is: {monthly_payment} rupees") 

#6. Factorial of a number
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1) 

# n = int(input("Enter a number to calculate its factorial: ")) 
# print(fact(n)) 


