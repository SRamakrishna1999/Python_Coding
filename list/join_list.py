list1=['a','b','c','d']
list2=[1,2,3,4]

list3=list1+list2
print(list3)

list4=[]
for x in list3:
    list4.append(x)
print(list4)   


list1.extend(list2)
print(list1)
