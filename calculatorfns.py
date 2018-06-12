def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def mod(a, b):
    return a % b


def floor(a, b):
    return a//b


def exp(a, b):
    return a**b


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
print(" 8.EXIT")
print(" ENTER YOUR CHOICE")
choice = int(input())
while choice != 8:
    if choice == 1:
        print(add(a, b))
    elif choice == 2:
        print(sub(a, b))
    elif choice == 3:
        print(mul(a, b))
    elif choice == 4:
        print(div(a, b))
    elif choice == 5:
        print(floor(a, b))
    elif choice == 6:
        print(exp(a, b))
    elif choice == 7:
        print(mod(a, b))
    else:
        print("INVALID CHOICE")
    print("Enter choice")
    choice = int(input())



