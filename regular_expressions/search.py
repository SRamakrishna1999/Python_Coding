import re

str='shiva rama krishina'

r1=re.search('a',str)
print(r1)

r2=re.search('shi',str)
print(r2)

r3=re.search('xyz',str)
print(r3)
