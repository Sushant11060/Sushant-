import re
d="String with different lengt# characters"
p=r'\b\w{1,5}\b'
res=re.findall(p,d)
print(res)
