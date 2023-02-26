l=int(input("enter last month reading: "))
c=int(input("enter current month reading: "))
r=l-c
print(r)
if(r<=100):
    print("the bill amount: ",r*3.46)
elif((r>=101)and(r<=500)):
    print("the bill amount: ",r*7.43)
else:
     print("the bill amount: ",r*10.32)
