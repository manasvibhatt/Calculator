import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def pow(a,b):
    return a**b
def div(a,b):
    return a/b
def sqrt(a):
    return math.sqrt(a)
print("Welcome to the simple calculator:")
print("1. Addition\t"+"2. Subtraction\t"+"3. Multiplication\t"+"4. Division\t"+"5. Power\t"+"6. Square Root\t"+"7.Quit")
while True:
    try:
        choice = int(input("Enter the function number:"))
        if (choice == 1):
            try:
                m = float(input("Enter first number: "))
                n = float(input("Enter second number: "))
                print(add(m, n))
            except ValueError:
                print("Oops! Try to enter a number.")
        elif (choice == 2):
            try:
                m = float(input("Enter first number: "))
                n = float(input("Enter second number: "))
                print(sub(m, n))
            except ValueError:
                print("Oops! Try to enter a number.")
        elif (choice == 3):
            try:
                m = float(input("Enter first number: "))
                n = float(input("Enter second number: "))
                print(mul(m, n))
            except ValueError:
                print("Oops! Try to enter a number.")
        elif (choice == 4):
            try:
                m = float(input("Enter first number: "))
                n = float(input("Enter second number: "))
                print(div(m, n))
            except ZeroDivisionError:
                print("Oops! Divide by zero error")
            except ValueError:
                print("Oops! Try to enter a number")
        elif (choice == 5):
            try:
                m = float(input("Enter first number: "))
                n = float(input("Enter second number: "))
                print(pow(m, n))
            except ValueError:
                print("Oops! Try to enter a number.")
        elif (choice == 6):
            try:
                m = float(input("Enter a number: "))
                print(sqrt(m))
            except ValueError:
                print("Oops! Try to enter a number.")
        elif (choice == 7):
            print("Please come back again")
            break
        else:
            print("Oops! Try to select from the menu")
    except ValueError:
        print("Please choose the choice number again")
