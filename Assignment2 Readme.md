# Task 1
🧮 Even or Odd Number Checker

This is a simple Python program that checks whether a given number is even or odd.

📘 Description

The program prompts the user to enter a number and then determines whether it is even or odd using the modulus operator (%).

🧠 How It Works

The program takes an integer input from the user.

It divides the number by 2 using the modulus operator (num % 2).

If the remainder is 0, the number is even.

Otherwise, it’s an odd number.

💻 Code
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

🚀 Example Output
Enter a number: 8
8 is an even number.

Enter a number: 7
7 is an odd number.

🧩 Requirements

Python 3.x

▶️ Run the Program

To run this program, open your terminal or command prompt and type:

python Task3.py

#Task 2
🔢 Sum of Numbers from 1 to 50

This simple Python program calculates the sum of all numbers from 1 to 50 using a for loop.

📘 Description

The program uses a loop to iterate through numbers from 1 to 50, adds them together, and prints the total sum.

🧠 How It Works

A variable sum_of_number is initialized to 0.

A for loop runs from 1 to 50 (inclusive).

Each number is added to the running total (sum_of_number).

Finally, the result is printed to the console.

💻 Code
sum_of_number = 0
for num in range(1, 51):
    # print(f"{num} number.")
    sum_of_number += num

print(f"The sum of numbers from 1 to 50 is: {sum_of_number}")

🚀 Example Output
The sum of numbers from 1 to 50 is: 1275

🧩 Requirements

Python 3.x

▶️ Run the Program

To execute the script, open your terminal or command prompt and type:

python Task4.py


