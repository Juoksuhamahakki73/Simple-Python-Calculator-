# This is importing the math module from
# the Python Library
import math

# This is the defined math symbols 
addition_math = ("+")
subtraction_math = ("-")
multiplication_math = ("×")
division_math = ("÷")

#This is for the two numbers that the user
# will input to do the calculations
num1 = ()
num2 = ()

# This is the answer after the calculations
answer_solution = ()

# This welcome the user to the calculator
print("Hello user!, Ready for some Python simple calculation?")
# This lets the user know that it can only do basic math
print("At this time, I can only do +, ×, -, and ÷")

# Get numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

while True:
    math_symbol = input("Enter the symbol: ")

    if math_symbol == '+':
        math_solution = int(num1) + int(num2)
        print(str(num1) + " + " + str(num2) + " = " + str(math_solution))
        break
    elif math_symbol == '-':
        math_solution = int(num1) - int(num2)
        print(str(num1) + " - " + str(num2) + " = " + str(math_solution))
        break
    elif math_symbol == '×':
        math_solution = int(num1) * int(num2)
        print(str(num1) + " × " + str(num2) + " = " + str(math_solution))
        break
    elif math_symbol == '÷':
        math_solution = int(num1) / int(num2)
        print(str(num1) + " ÷ " + str(num2) + " = " + str(math_solution))
        break
    else:
        print("Sorry, that is the incorrect input I was looking for, please try again.")
