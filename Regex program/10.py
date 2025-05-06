import re
d="string having letter a"
p=r'[^a]'
res=re.findall(p,d)
print(res)
