"""n=5;i=0
while(i<=n):
    print(" " * (n - i) +"*" * i)
    i+=1
"""
def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = 5
triangle(n)
