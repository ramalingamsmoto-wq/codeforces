

def process(a,b,c):
    aux=[]
    aux.append((a,b,c))
    aux.append((a,b,a+b))
    aux.append((a,a+c,c))
    aux.append((b+c,b,c))
    
    limit=(2**65)
    ans=limit
    for tup in aux:
        mx=max(tup)
        mn=min(tup)
        v1=mx-mn
        ans=min(ans,v1)
        
    return ans    
        
    

t=int(input())
res=[]
for _ in range(t):
    a,b,c=map(int,input().strip().split())
    tans=process(a,b,c)
    res.append(tans)
    
for e in res:
    print(e)