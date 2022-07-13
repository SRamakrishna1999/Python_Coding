x=(1,2,3,4,5,6,7,8)

y=list(x)
y[0]=0
x=tuple(y)
print(x)

y.append(9)
x=tuple(y)
print(x)

z=(10,11)
x+=z
print(x)

y=list(x)
y.remove(11)

x=tuple(y)
print(x)
