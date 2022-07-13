list1=['siva','rama','krishna','siri','ayyappa']

for x in list1:
    print(x)

for i in range(len(list1)):
    print(list1[i])

n=0
while n<len(list1):
    print(list1[n])
    n=n+1

#list comprehensiton is nothing but reduce the syntax

[print(x) for x in list1]
