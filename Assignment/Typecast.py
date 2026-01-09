#take user input for a float and an integer, then print their sum after typecasting the float to an integer.

a = float(input("Enter a float number: "))
b = int(input("Enter an integer number: "))
sum = int(a) + b #typecasting float to int before addition
print(f"The sum of {a} and {b} is {sum}")
