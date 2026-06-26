f = open("data.txt", "r") 
data = f.read() 
print(data) 
f.close() 

with open("data.txt", "r") as f:
    data = f.readline()
    while data:
        print(data)
        data = f.readline() 

with open("data.txt", "r") as f:
    for line in f:
        print(line) 

file = open("sample.txt", "w") 
file.write("Hello, World!\n") 
file.write("Welcome to file handling in Python.\n")
file.close() 

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines) 

name = "John"
age = 30
with open('output.txt', 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n") 

f = open("products.txt","a") 
f.write("Chocolates\n")
f.write("Cookies\n")
f.write("Ice Cream\n")  
f.close() 

with open('data.txt', 'r') as file:
    file.seek(10)  
    data = file.read() 
    print(data) 

with open('output.txt', 'r') as file:
    position = file.tell()
    print(f"Current position: {position}")  

with open('products.txt', 'r') as file:
    file.seek(0,2)
    size = file.tell()
    print(f"Size of the file: {size} bytes") 

import os
current_name = 'Products.txt'
new_name = 'Items.txt'
os.rename(current_name,new_name) 

import os
file_to_delete = 'output.txt'
os.remove(file_to_delete) 

try:
    with open('products.txt', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist.")  

try:
    with open('products.txt', 'r') as file:
        data = file.read()
        print(data) 
        
except FileNotFoundError:
    print("The file does not exist.") 

except PermissionError:
    print("You do not have permission to access this file.")

except IOError:
    print("An I/O error occurred while handling the file.") 

import json
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
with open('hdfc_loan_sample_20_rows.json','w') as f:
    json.dump("data.txt",f)  
