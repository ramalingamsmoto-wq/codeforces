

res=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    v1=max(a)-min(a)
    res.append(v1)
    
for e in res:
    print(e)    