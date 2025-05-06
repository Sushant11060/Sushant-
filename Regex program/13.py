import re
d="string654 w1th 98number$87654"
p=r'\d+'
res=re.findall(p,d)
print(res)
