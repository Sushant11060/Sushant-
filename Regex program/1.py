import re
d="python is a programming language"
p="python"
res=re.match(p,d,re.IGNORECASE)
if res:
    print("starts with python")
else:
    print("doesn't starts with python")
