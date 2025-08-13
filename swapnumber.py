# to swap two numbers

num1= int(input("Enter a numer: "))
num2 = int(input("Enter another number: "))

print(f"Before swaping: {num1} , {num2}")

num1, num2 = num2, num1
print(f"After swaping: {num1} , {num2}")

