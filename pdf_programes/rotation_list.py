l1=[]

length=int(input('enter length of the list\n'))

for x in range(length):
    l1.append(int(input()))

print('before rotation')
print(l1)

#print('please enter  rotation range\n')

n=int(input('please enter  rotation range\n'))

for x in range(n):
    element=l1.pop(0)
    l1.append(element)

print('after rotation')
print(l1)

