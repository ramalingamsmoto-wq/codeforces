

def process(n):
    
    cnt=0
    
    for i in range(1,n,1):
        v1=i
        for j in range(1,n,1):
            v2=n-j
            if v1==v2:
                cnt=cnt+1
                
    return cnt        
            



res=[]
for _ in range(int(input())):
    n=int(input())
    tans=process(n)
    res.append(tans)
    
for e in res:
    print(e)    
    