a=int(input("enter a num"))
b=int(input("enter a num"))
op=input("enter a operator")
if(op=='+'):
    def add(a,b):
        c=a+b
        return c
    c=add(a,b)
    print(c)
elif(op=='-'):
    def sub(a,b):
        c=a-b
        return c
    c=sub(a,b)
    print(c)
elif(op=='*'):
    def mult(a,b):
        c=a*b
        return c
    c=mult(a,b)
    print(c)
else:
    def dev(a,b):
        c=a/b
        return c
    c=dev(a,b)
    print(c)
