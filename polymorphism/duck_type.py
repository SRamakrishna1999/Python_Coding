class car:

    def execute(self):
        print('Blue colour')
        print('BMW')

class fruits:

    def execute(self):
        print('apple')
        print('banana')


class my_fun:

    def detail(self,ide):
        ide.execute()

ide=car()

infor=my_fun()

infor.detail(ide)
