print("Enter any sentence")
x = input()
data = map(lambda z: z.upper(), x.split(' '))
print(list(data))