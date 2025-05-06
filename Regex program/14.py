import re
d="a 1ph@ n um 3r$ic"
p=r'\w\w+'
res=re.findall(p,d)
print(res)
