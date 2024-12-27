n=10
list=[]
for i in range(0,n,2):
    print(" "*(n-i-1),end="")
    print("*"*(i+1))
print()
for i in range(0,n,2):
    print("*"*(i+1),end="")
    print(" "*(n-i-1))
    
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()