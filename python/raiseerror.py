a = float(input("Enter a number: "))
b = float(input("Enter a second number: "))

if b == 0:
    raise ZeroDivisionError("Sir, don't enter zero!")
else:
    print(f"The output is {a / b}")
