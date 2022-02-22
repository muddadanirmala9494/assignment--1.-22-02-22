# assignment--1.-22-02-22


n=int(input('enter number:'))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" * ",end=" ")
    print("\n")
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(n-i,0,-1):
        print("   *",end="")
    print("\n")
