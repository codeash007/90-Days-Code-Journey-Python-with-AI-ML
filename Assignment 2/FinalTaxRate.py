Salary = float(input("Enter your salary: "))
if Salary < 30000:
    TaxRate = 5 / 100
elif 30000 <= Salary <= 70000:
    TaxRate = 15 / 100
elif Salary > 70000:
    TaxRate = 25 / 100
TaxAmount = Salary * TaxRate
print("Your tax amount is: ", TaxAmount)