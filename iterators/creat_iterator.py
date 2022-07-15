class iterator_func():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return x

my_iter=iterator_func()
#print(my_iter)
iterator=iter(my_iter)
#print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

