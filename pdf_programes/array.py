a=[]
b=[]

length=int(input('enter length of the array\n'))

for x in range(length):
    a.append(int(input()))
print('array of elements')
print(a)

for index in range(len(a)-1):
    if a[index]>a[index+1]:
        b.append(a[index])

print('after checking right most values grater than in array')

print(b)

    
