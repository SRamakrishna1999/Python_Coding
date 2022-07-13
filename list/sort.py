list1=['siva','rama','krishna','siri','ayyappa']
list2=[40,54,2,34,13,57,75]

list1.sort()
print(list1)
list2.sort()
print(list2)

#dessending order
list1.sort(reverse=True)
print(list1)
list2.sort(reverse=True)
print(list2)

def fun(n):
    return abs(n-50)

list2.sort(key=fun)
print(list2)

list1.reverse()
print(list1)
