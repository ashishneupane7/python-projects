# name="Asmita"
# grade=12
# section="mgmt"
# a="Yes"
# if a == "No":
#     print(name,"from",grade,section,"is Present")
# else:
#     print(name,"from",grade,section,"is Absent")

# print("Thank You!!")

# def am(a,b):
#     print((a+b)/2)

# am(2,3)
'''
Hoosnskdddkfnnjfjkdms
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
