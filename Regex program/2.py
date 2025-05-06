import re
d="c++ c java python etc."
p="python"
res=re.search(p,d,re.IGNORECASE)
if res:
    print("contains <python>")
else:
    print("does't contains <python>")
