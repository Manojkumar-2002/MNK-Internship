l=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
x=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
z=[[0 for j in range(len(x[0]))] for i in range(len(x))]
for i in range(len(l)):
    for j in range(len(x[0])):
        for k in range(len(x)):
            z[i][j]+=l[i][k] * x[k][j]
        
        
print(z)
for i in range(len(l)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] + l[i][j]
print(z)

for i in range(len(l)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j]-l[i][j]
print(z)