try:
   lst=[0,1,2,3,4,5,6,7]
   i=int(input("Enter index: "))
   print("Value at given index: ",lst[i])
except IndexError:
    print("Please enter a valid index")
