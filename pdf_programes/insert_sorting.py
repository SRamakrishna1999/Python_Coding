a=[]
b=[]

length1=int(input('enter a list length\n'))
for x in range(length1):
    a.append(int(input()))

length2=int(input('enter b list length\n'))

for x in range(length2):
    b.append(int(input()))

for x in range(len(b)):
    a.append(b[x])
print("before sorting")
print(a)

'''for x in range(len(a)-1):
    if a[x] > a[x+1]:
        temp=a[x]
        a[x]=a[x+1]
        a[x+1]=temp'''
print('after sorting')
a.sort()
print(a)

