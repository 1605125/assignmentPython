temp = []
def extract (l1):
    for i in l1:
        if isinstance(i,list):
            extract(i)
        else:
            temp.append(i)
