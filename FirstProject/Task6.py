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