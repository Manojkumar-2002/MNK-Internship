l=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n=len(l)
m=len(l[0])
res= []
top,bottom=0,n-1
left, right = 0,m-1
while left<=right and top<=bottom:
    for i in range(left,right+1):
        res.append(l[top][i])
        print("l-r",l[top][i])
    top+=1
    for j in range(top,bottom+1):
        res.append(l[j][right])
        print("t-b",l[j][right])
    right-=1 
    if top<=bottom:
        for k in range(right,left-1,-1):
            res.append(l[bottom][k])
            print("r-l",l[bottom][k])
        bottom-=1
        
    if left<=right:
        for z in range(bottom,top-1,-1):
            res.append(l[z][left])
            print("b-t",l[z][left])
        left+=1
print("spiral",res)
res=[res[-1]]+res[:-1]
rot=[]
for i in range(n):
    rot.append(res[i*m:(i+1)*m])


print("rotated spiral",rot)
