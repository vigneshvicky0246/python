list=[1,2,3,4,5,6,7,8]
evenlist = [] 
oddlist = [] 
for i in list: 
  if (i % 2 == 0): 
    evenlist.append(i)
  else: 
    oddlist.append(i) 
print("Even lists:", evenlist) 
print("Odd lists:", oddlist)
