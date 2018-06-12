# read one file and convert it to upper
lst=[]
with open("check.py", 'r') as f:
    for line in f:
        print(line)
        l = line.upper()
        print(l)
        lst.append(l)

print(lst)
with open("check1.py", 'w') as out:
    out.writelines(lst)

