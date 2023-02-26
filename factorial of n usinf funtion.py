n=int(input("enter a number"))
def fact(n):
    if (n==1):
        return 1
    else:
        return n*fact(n-1)
fact=fact(n)
print(fact)

 
