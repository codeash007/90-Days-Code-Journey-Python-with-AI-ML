a = int(input("Enter first number:"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

def avg_num(a , b , c ):
    avg = (a + b + c)/3
    print(f"The Average of Three Number is:",{avg})
avg_num(a , b , c)