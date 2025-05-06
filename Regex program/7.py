import re
d="numbers 12 123 1234 456"
p=r'\b\d{3}\b'
res=re.findall(p,d)
print(res)
