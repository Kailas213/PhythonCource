<<<<<<< HEAD
def factorial(factNum):
    fact=1
    for i in range(1,factNum+1):
        fact =fact*i
    return fact

factNum = int(input("Enter a number:"))
result=factorial(factNum)
print(f"Factorial of {factNum} is {result}")






=======
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
>>>>>>> b2f3e97f1a15382fd7c177fb6d64a252862efc5f
