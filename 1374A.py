
def process(x,y,n):
    q=n//x
    
    for i in range(q,-1,-1):
        v1=(i*x)+y
        if v1 <=n:
            return v1
    return -1
              



t=int(input())
res=[]
for _ in range(t):
    
    x,y,n=map(int,input().strip().split())
    tans=process(x,y,n)
    res.append(tans)
for e in res:
    print(e)    