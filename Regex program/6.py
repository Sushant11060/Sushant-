import re
d="Alphanumeric@#123^%$"
p=r'[0-9a-zA-Z]'
res=re.findall(p,d)
print(res)
