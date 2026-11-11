t=int(input())
res=[]
for i in range(t):
    a=list(map(int,input().strip().split()))
    a.sort()
    if a[1] +a[2] >= 10:
        res.append("YES")
    else:
        res.append("NO") 
for e in res:
    print(e)           