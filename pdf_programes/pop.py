list=[]
length=int(input('enter list length\n'))

for x in range(length):
    list.append(int(input()))

print('before using pop')
print(list)

pop=int(input('enter pop index value\n'))

list.pop(pop)
print('after using pop')
print(list)

