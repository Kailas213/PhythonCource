Factorial Calculator in Python

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


Enter any positive integer when prompted.

📌 Example Output
Enter a number: 5
Factorial of 5 is 720
