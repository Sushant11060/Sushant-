try:
   d={"a":"apple","b":"ball","c":"cat"}
   k=input("Enter the key:")
   print(d[k])
except KeyError:
    print("Please enter a valid key")
