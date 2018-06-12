olst = []
# for i in range(0,7):
#     inlst = []
#     inlst.append(i)
#     inlst.append(i+1)
#     olst.append(inlst)
# print(olst)
olst = [['q','i',9],[3,4],[3,4,'abc','xyz',[100,[101,102,[103]]]]]
single_lst = []
for ele in olst:
    if type(ele) == list:
        for e in ele:
            single_lst.append(e)
    else:
        single_lst.append(ele)
print(single_lst,end=' ')





