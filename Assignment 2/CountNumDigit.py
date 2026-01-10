n = int(input("Enter a number: "))
count = 0
def count_digits(n):
    global count # Use global keyword to modify the global variable
    while n > 0:
        n = n // 10
        count += 1
count_digits(n)
print(f"The number of digits in the given number is: {count}")
    