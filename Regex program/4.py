import re
d="There ArE sOMe UPPERcase Characters in thIS stRing"
p=r'[A-Z]'
res=re.findall(p,d)
print(res)
