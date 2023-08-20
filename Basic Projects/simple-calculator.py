'''
Some info about project:
Name of Project: Simple Calculator for addition, subraction, multiplication, division using python.
Project By: Ashish Neupane
Language: Python
Created on: 2023/04/14
Uploaded on Github: 2023/08/20
***This Project was made after I learned basic of Python.***
'''

num1 = input("Enter First Number: ")
operation = input("Select Operation(+, -, *, /): ")
num2 = input("Enter Second Number: ")

add = int(num1) + int(num2)
subtract = int(num1) - int(num2)
multiply = int(num1) * int(num2)
divide = int(num1) / int(num2)

if operation == "+":
    print ("Your result is:",add)

elif operation == "-":
        print("Your result is:",subtract)

elif operation == "*":
    print("Your result is:",multiply)

elif operation == "/":
    print("Your result is:",divide)

else:
    print("Error!! Invalid input")
