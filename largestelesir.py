size = int(input("size \n"))
l1 = []
while size:
    num = input("Number? \n")
    if num.isalpha():
        continue
    l1.append(int(num))
    size -= 1
max = l1[0]
for i in l1:
    if i > max:
        max = i
print(max)