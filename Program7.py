try:
    fname=input("Enter file name: ")
    f=open(fname)
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Please enter a valid file name") 
