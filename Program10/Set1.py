myset=set()

def slen2():
    return len(myset)

def adds2(x):
    myset.add(x)
    return myset

def remove2(x):
    if x in myset:
        myset.remove(x)
        return myset
    else:
        return "element not found in the set"
