s=int(input("enter a salary: "))
y=int(input("enter a working year: "))
print(s)
print(y)
if(y<5):
    print("no bonus",s)
else:
    print("your bonus: ",(s*0.05))
    print("your bonus with salary ",(s*0.05)+s)

