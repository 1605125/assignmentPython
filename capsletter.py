print("Enter any sentence")
x = input()

# Expression for varname in sequence condition
data = [i for i in x if i.isalpha() and i.isupper()]

print(list(data))
