t=int(input("enter a total class: "))
a=int(input("enter a attened days: "))
att=(a/t)*100
print(att)
if(att<75):
    med=input("medical issuess yes/no")
    if(med=='no'):
        print("you r not eligible")
    else:
        print("you r eligible")
else:
    print("you r eligible")
