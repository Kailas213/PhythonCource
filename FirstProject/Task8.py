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
