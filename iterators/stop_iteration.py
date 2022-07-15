class iterator_func():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a <= 10:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_iter=iterator_func()
nice=iter(my_iter)
for i in nice:
    print(i)
