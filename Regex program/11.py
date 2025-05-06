import re
d="$pe(i@l ch@rac!ers&"
p=r'[^\w\s]'
res=re.findall(p,d)
print(res)
