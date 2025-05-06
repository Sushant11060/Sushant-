import re
d="There ArE LOWERcase CHARACterS"
p=r'[a-z]'
res=re.findall(p,d)
print(res)
