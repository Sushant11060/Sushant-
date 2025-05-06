import re
d="123 12345 123456 1234567 1234"
p=r'\b\d{1,5}\b'
res=re.findall(p,d)
print(res)
