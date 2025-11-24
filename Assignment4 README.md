# Task 1

# File Reader with Error Handling in Python

This Python program demonstrates how to read a file line by line while handling errors gracefully.
If the file (sample.txt) exists, the program prints each line along with its line number.
If the file is missing, it shows a user-friendly error message instead of crashing.

📌 Features

Reads a text file safely

Displays line numbers for each line

Handles missing file errors with try-except

Uses enumerate() for cleaner iteration

📜 Code
from operator import index

try:
    # Opening the file
    file = open("sample.txt", "r")
    print("Reading file content:")
    
    # Reading and printing content line by line
    for index, line in enumerate(file):
        print(f"Line {index+1}: {line.strip()}")  # strip() removes extra newline
    
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

▶️ How to Run

Create a text file named sample.txt in the same folder as your Python script.

Add some sample text to the file.

Save your Python script as Task7.py.

Run the script:

python Task7.py

📌 Example Output

If the file exists:

Reading file content:
Line 1: This is line one.
Line 2: This is line two.
Line 3: Another line of text.


If the file does not exist:

Error: The file 'sample.txt' was not found.

💡 Notes

Always ensure the file path is correct.

# Task 2

File Write, Append, and Read Program in Python

This Python program demonstrates how to write, append, and read data from a file named output.txt.
The user enters text, which is saved to the file, and then additional text is appended.
Finally, the program reads and displays the complete content of the file.

📌 Features

Takes user input and writes it to a file

Appends more data without deleting existing content

Reads the file and prints the final result

Uses Python’s with open() for safe file handling

📜 Code
# Taking user input and writing to a file
text = input("Enter text to write to file: ")

# Writing to the file
with open("output.txt", "w") as file:
    file.write(text + "\n")
    print("Data Successfully written to output.txt.\n")

# Appending additional text
append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
    print("Data Successfully append.\n")

# Reading and displaying final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

▶️ How to Run

Save the script as Task8.py.

Run the script:

python Task8.py


Enter text when prompted.

Check output.txt to see the stored content.

📌 Example Output
Enter text to write to file: Hello, paython!
Data Successfully written to output.txt.

Enter additional text to append: Learning file handling in python.
Data Successfully append.


Final content of output.txt:
Hello, paython!
Learning file handling in python.

💡 Notes

"w" mode overwrites the file every time.

"a" mode adds new data without deleting old text.

strip() is used to remove extra newline characters for clean display.

Using strip() removes trailing newline characters for clean output.

enumerate() automatically tracks the line numbers.
