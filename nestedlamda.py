print("Enter first number ")
f1 = int(input())
print("Enter second number ")
f2 = int(input())
print("Enter third number ")
f3 = int(input())
data = lambda a, b, c: a if a > b and a > c else b if b > c else c


print("The largest is {}".format(data(f1, f2, f3)))

