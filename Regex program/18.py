import re
d="akash@gmail.com kamal267@outlook.com deepak367@yahoo.com raghav27627@mail34.com"
p=r'\w+@[a-zA-Z]+\.com'
res=re.findall(p,d)
print(res)
