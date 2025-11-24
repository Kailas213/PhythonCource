from operator import index

try:
    # Opening the file
    file = open("sample.txt", "r")
    print("Reading file content:")
    # Reading and printing content line by line
    for index, line in enumerate(file):
        print(f"Line {index+1}:{line.strip()}")  # strip() removes extra newline
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")