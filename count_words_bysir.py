String = 'hi hello you in hello'
data = String.split(' ')
d1 ={}
for word in data:
    d1[word] = data.count(word)
print(d1)