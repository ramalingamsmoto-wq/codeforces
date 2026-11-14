

def process(n):
    q=n//2020
    r=n%2020
    if  r<= q:
        return "YES"
    return "NO"    
    
    
            


t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    tans=process(n)
    res.append(tans)
for e in res:
    print(e)    
    