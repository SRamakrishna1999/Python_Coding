class siva:

    def __init__(self):
        self.name='ram'
        self.age='22'

    def compair(self,c2):
        if self.age==c2.age:
            return True
        else:
            return False



c1=siva()
#c1.age=23
c2=siva()

if c1.compair(c2):
    print('same')

else:
    print('not same')
