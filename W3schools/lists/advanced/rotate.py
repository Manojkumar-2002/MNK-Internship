l=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n=len(l)
m=len(l[0])
flat = [j for i in l for j in i]
flat = [flat[-1]]+flat[:-1]
print(flat)
res=[]
for i in range(n):
    res.append(flat[i*m:(i+1)*m])
print(res)
    