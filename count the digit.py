num=int(input("enter a number"))
count=0
while num!=0:
    num//=10
    count=count+1
print(count)
