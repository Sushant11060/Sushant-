lst=[]

def append1(x):
    lst.append(x)
    return lst

def extend1(l):
    lst.extend(l)
    return lst

def pop():
    if lst:
        return lst.pop()
    else:
        return "List is empty."

def remove1(x):
    if x in lst:
        lst.remove(x)
        return lst
    else:
        return "element not found in the list"
