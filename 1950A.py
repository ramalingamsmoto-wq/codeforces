t=int(input())
res=[]
for _ in range(t):
    a,b,c=map(int,input().strip().split())
    if a<b<c:
        res.append("STAIR")
    elif a<b>c:
        res.append("PEAK")
    else:
        res.append("NONE")  
        
for e in res:
    print(e)          