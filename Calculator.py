print("Enter the first number")
a = input()
while not a.isdigit():
    print("Enter digits as your input for first number")
    a = input()
a = int(a)
print("Enter the second number")
b = input()
while not b.isdigit():
    print("Enter digits as your input for first number")
    b = input()
b = int(b)
print("*******MENU*******")
print(" 1.ADD")
print(" 2.SUBTRACT")
print(" 3.MULTIPLY")
print(" 4.DIVISION")
print(" 5.FLOOR DIVISION")
print(" 6.EXPONENT")
print(" 7.MODULUS")
print(" 8.ENTER YOUR CHOICE")
choice = input()
choice = int(choice)
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a/b)
elif choice == 5:
    print(a//b)
elif choice == 6:
    print(a ** b)
elif choice == 7:
    print(a % b)
else:
    print("INVALID CHOICE")
