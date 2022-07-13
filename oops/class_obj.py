class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print(self.cpu,self.ram)

    def configu(self):
        print('configu is',self.cpu,self.ram)

a= computer('i5',32)
b= computer('ryzon 3',64)

a.configu()
b.configu()
        
