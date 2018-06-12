# program to count repeated words and c opy it to another file


from collections import Counter
from json import dumps, loads

def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())

temp = word_count("check.py")
print("temp {}".format(temp))
with open('test', 'w') as file:

    file.writelines(dumps(dict(temp)))
print("Number of words in the file :", dumps(dict(temp)))


with open('test') as file:

    temp2 = file.read()
    temp2 = loads(temp2)
    print(temp2['hi'])