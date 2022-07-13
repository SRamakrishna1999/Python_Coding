list1=['siva','rama','krishna']
list2=['vijay','yash','sebin','gnanadeep','prabhat']
list3=('ramayya','rajesh','mani')
list1.append('siri')
print(list1)

list1.insert(1,'ayyappa')
print(list1)

list1.extend(list2)
print(list1)

# extend method using tuple,set,dictionary items are added in list

list1.extend(list3)
print(list1)


