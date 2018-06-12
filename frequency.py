
print("Enter the number of words you want to enter for list")
x = int(input())
i = 0
lst = []
while i < x:
    print("Enter the value")
    y = input()
    lst.append(y)
    i += 1
print(lst)
# nlst = lst.copy()
# i = 0
# j=0
# count = 0
# while i < len(lst):
#     count [i] = lst.count(nlst[i])
#     i += 1
# while j < len(lst):
#     print("{}          {}".format(lst[i],count[i]))
nlst = []
for num in lst:
    if num not in nlst:
        nlst.append(num)
print(nlst)
i, j = 0
c = []
while j<len(nlst):
    k=0
    while i < len(lst):
        if lst[i] == nlst[j] :
            k += 1
            c[i] = k
        i += 1
    j += 1
m = 0
while m < len(nlst):
    print(nlst[i])







