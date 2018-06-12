# assignment 3
# Program to read size from the keyboard and ask for element for array list and find the largest element in the list
print("ENTER THE SIZE OF ARRAY LIST")
x = int(input())
i = 0
lt = []
while i < x:
    print("enter value for list {}".format(i))
    v = input()
    lt.append(v)
    i += 1
print("The list is",end='')
print(lt)
lst = []
for m in lt:
    if m.isdigit():
        lst.append(m)
print("The number list is {}".format(lst))
# print(max_num_in_list(lst))

max_val = int(lst[0])
for item in lst:
    if int(item) > int(max_val):
        max_val = int(item)
print("The largest number is {}".format(max_val))
