import re

str='shiva rama krishna'

result=re.findall('a',str)

print(result)

r1=re.findall('sh',str)
print(r1)

r2=re.findall('xyz',str)
print(r2)

