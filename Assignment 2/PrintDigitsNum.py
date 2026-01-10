Number = int(input("Enter a number: "))
def printdigit(Number):
    while Number > 0:
        digit = Number % 10
        print(digit)
        Number = Number // 10
printdigit(Number)