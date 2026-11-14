t=int(input())
limit=(2**70)
res=[]
for _ in range(t):
    a,b=map(int,input().strip().split())
    mn=limit
    for c in range(a,b+1,1):
        t=(c-a)+(b-c)
        mn=min(mn,t)
    res.append(mn)
for e in res:
    print(e)    