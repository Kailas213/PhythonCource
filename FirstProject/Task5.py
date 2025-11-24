def factorial(factNum):
    fact=1
    for i in range(1,factNum+1):
        fact =fact*i
    return fact

factNum = int(input("Enter a number:"))
result=factorial(factNum)
print(f"Factorial of {factNum} is {result}")
