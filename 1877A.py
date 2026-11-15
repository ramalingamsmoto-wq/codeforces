
res=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    s=sum(a)
    res.append(-s)
    
for e in res:
    print(e)    
    