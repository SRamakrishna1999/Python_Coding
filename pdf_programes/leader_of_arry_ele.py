a=[]
b=[]

length=int(input('enter length of the elements\n'))
for x in range(length):
    a.append(int(input()))

print('list elements')
print(a)

for index in range(0,len(a)-1):
    if(a[index]<a[index+1]):
        #if(a[index+2]<a[index+3]):
            #b.append(a[index+2])
        b.append(a[index+1])

print('leadr values in list')
print(b)
