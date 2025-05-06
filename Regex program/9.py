import re
d="consonAnts String"
p=r'[b-df-hj-np-tv-z]'
res=re.findall(p,d)
print(res)
