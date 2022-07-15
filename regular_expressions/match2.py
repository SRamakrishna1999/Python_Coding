import re

str='siva rama krishna'

r1=re.match(r'siva',str)

if r1:
    print('match found:',r1)

else:
    print('not found:',r1)
