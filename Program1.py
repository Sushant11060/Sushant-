try:
    a=int(input("Enter divident: "))
    b=int(input("Enter divisor: "))
    res=a/b
    print("Result: ",res)
except ZeroDivisionError:
    print("Please enter a non zero divisor")
