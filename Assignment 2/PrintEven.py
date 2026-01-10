a = int(input("Enter first number:"))
b = int(input("Enter second number :"))
def evennum (a , b):
    for num in range (a , b+1):
        if num % 2 == 0:
            print(f"Even number is: {num}")
evennum (a , b)


