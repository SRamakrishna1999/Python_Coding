class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,others):
        m1=self.m1+others.m1
        m2=self.m2+others.m2
        s3=student(m1,m2)

        return s3


s1=student(34,53)
s2=student(36,45)

s3=s1+s2
print(s3.m1)
