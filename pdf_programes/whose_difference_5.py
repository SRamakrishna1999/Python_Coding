a=[]
length=int(input('enter length of array\n'))

for x in range(length):
    a.append(int(input()))

print(a)

b=[]

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        temp=a[i]-a[j]
        if temp==5 or temp==-5:  # sorting arry condition temp==5
            b.append(a[i])
            b.append(a[j])


print(b)            

