t=int(input())
res=[]
for _ in range(t):
    x,y=map(int,input().strip().split())
    tans=f"{min(x,y)} {max(x,y)}"
    res.append(tans)
    
for e in res:
    print(e)    