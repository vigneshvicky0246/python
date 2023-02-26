a=int(input("enter a string: "))
s=0
temp=a
while temp<0:
    digit=temp%10
    s=digit**3
    temp//=0
if(a==s):
    print(a," is not a armstrong num")
else:
    print(a,"is  a armstrong num")  
