import re
d="string with different lenths of words"
p=r'\b\w{2,4}\b'
res=re.findall(p,d)
print(res)
