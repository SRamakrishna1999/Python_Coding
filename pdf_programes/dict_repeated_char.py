str=input('please enter string\n')
dict = {}

for eachChar in range(len(str)):
    if str[eachChar] in dict:
        dict[str[eachChar]]+= 1
    else:
        dict[str[eachChar]] = 1

print(dict)        
