
def process(n,k):
    s=0
    a=[k]
    
    while True:
        
        s=sum(a)
        q=s//n
        v1=sum(a[1:])
        v2=q-v1
        print(f"q {q} s {s} k {k} v1 {v1} v2 {v2}")
        if s-q==k:
            break
            
        
        a.append(v2)
        
        
    ans=sum(a)    
   # print(*a)  
    return ans  
        
        
        


t=int(input())
res=[]
for i in range(t):
    n,k=map(int,input().strip().split())
    tans=process(n,k)
    res.append(tans)
for e in res:
    print(e)    