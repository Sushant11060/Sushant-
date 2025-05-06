try:
    import meth as m
    print("Square root of 25 = ",m.sqrt(25))
except ModuleNotFoundError:
    print("Not a valid module name")
