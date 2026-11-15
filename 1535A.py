t=int(input())
res=[]
for _ in range(t):
    a,b,c,d=map(int,input().strip().split())
    
    l1=[a,b]
    l2=[c,d]
    
    if max(l1)<=min(l2) or max(l2)<=min(l1):
        res.append("NO")
    else:
        res.append("YES")   
        
for e in res:
    print(e)         
    