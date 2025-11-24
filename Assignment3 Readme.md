#Task 1

#Factorial Calculator in Python

This Python program calculates the factorial of a number using a user-defined function.
The program accepts a number from the user, computes the factorial using a loop, and displays the result.

📌 Features

Uses a custom function factorial()

Calculates factorial using a for loop

Takes user input

Simple and beginner-friendly

🧮 What is Factorial?

The factorial of a number n is:

n! = 1 × 2 × 3 × ... × n


Example:
5! = 120

📜 Code
def factorial(factNum):
    fact = 1
    for i in range(1, factNum + 1):
        fact = fact * i
    return fact

factNum = int(input("Enter a number: "))
result = factorial(factNum)
print(f"Factorial of {factNum} is {result}")

▶️ How to Run

Save the script as Task5.py

Run the program:

python Task5.py

📌 Example Output
Enter a number: 5
Factorial of 5 is 720


#Task 2
Math Module Calculations in Python

This Python program demonstrates how to use the math module to perform common mathematical operations such as finding the square root, natural logarithm, and sine value of a number.
The user provides a number as input, and the program displays the calculated results.

📌 Features

Accepts user input

Uses Python's built-in math module

Calculates:

Square Root

Natural Logarithm (base e)

Sine (in radians)

Beginner-friendly and easy to understand

📜 Code
import math

# Asking user for input
num = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)      # log base e
sine_value = math.sin(num)       # input in radians

# Displaying results
print(f"Square Root: {square_root}")
print(f"Logarithm: {natural_log}")
print(f"Sine: {sine_value}")

▶️ How to Run

Save the program as math_calculations.py

Run the file using:

python math_calculations.py


Enter any valid numeric value when prompted.

📌 Example Output
Enter a number: 10
Square Root: 3.1622776601683795
Logarithm: 2.302585092994046
Sine: -0.5440211108893698


Enter any positive integer when prompted.

