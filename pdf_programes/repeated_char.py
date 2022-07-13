str1=input('please enter string\n')

count=1     #str1.count(str1[0])
temp=''
ch=str1[0]
#print(str1.count(str1[0]))
#print(count)
#print(str1[0])
for x in str1:
    if x not in temp:
        #print(str1.count(x))
        if str1.count(x)>count:
            #print(str1.count(x))
            count=str1.count(x)
            ch=x

    temp=temp+x
#print(temp)
print(ch,count)    
    
