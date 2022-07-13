class a:

    def show(self):
        print("a in show")


class b(a):
    #pass
    def show(self):
        print("b in show")


s=b()

s.show()
