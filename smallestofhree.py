a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print(f"The smallest number is {smallest}.")
