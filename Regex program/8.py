import re
d="a sample string using vowels"
p=r'[aeiou]'
res=re.findall(p,d,re.IGNORECASE)
print(res)
