single_lst = []
def nestedList(olst):

    for ele in olst:
        if type(ele) == list:
            nestedList(ele)
        else:
            single_lst.append(ele)
    return single_lst
def singlelst():
    lst = [['q','i',9],[3,4],[3,4,'abc','xyz',[100,[101,102,[103]]]]]
    data = nestedList(lst)
    print(data)
singlelst()