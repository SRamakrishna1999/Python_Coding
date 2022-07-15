import re

str='siva rama krishna'

r1=re.sub('a','l',str)
print(r1)

r2=re.sub('rama','siri',str)
print(r2)

r3=re.sub('r','m',str,1)
print(r3)
