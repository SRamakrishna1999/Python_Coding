def fun(n):
    return lambda a: a*n

lamb_input=fun(10)

print(lamb_input(2))
