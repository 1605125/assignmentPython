class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

    def mod(self):
        return self.a % self.b

    def floor(self):
        return self.a // self.b

    def exp(self):
        return self.a ** self.b


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
obj = Cal(a, b)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Floor")

    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(), 2))
    elif choice == 5:
        print("Result: ", obj.mod())
    elif choice == 6:
        print("Result: ", obj.exp())
    elif choice == 7:
        print("Result: ", obj.floor())

    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()