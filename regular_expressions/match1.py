import re

line='siva rama krishna'

result1=re.match(r'rama',line)

print('on failur:',result1)

result2=re.match(r'siva',line)

print('on success:',result2)
