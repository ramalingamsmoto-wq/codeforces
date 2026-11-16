


def process(n,m,x,s):
    
    cnt=0
    
    if n<m:
        while True:
            l=len(x)
            if l>= m:
                break
            x=x+x
            cnt=cnt+1
            
    idx=x.find(s)      
    if idx==-1:
        x=x+x
        cnt=cnt+1
        
    idx=x.find(s)   
    if idx>=0:
        return cnt
    return -1    
              

t=int(input())

res=[]
for _ in range(t):
    n,m=map(int,input().strip().split())
    x=input()
    s=input()
    tans=process(n,m,x,s)
    res.append(tans)
    
for e in res:
    print(e)    