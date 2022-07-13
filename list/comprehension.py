list1=['siva','rama','krishna','siri']
new_list=[]
for x in list1:
    if 'a' in x:
        new_list.append(x)
        
print(new_list) 

new_list1=[x for x in list1 if 'a' in x]
print(new_list1)

new_list3=[x for x in list1 if x!='siva']
print(new_list3)
