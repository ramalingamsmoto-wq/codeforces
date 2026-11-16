
from collections import Counter



def process(n,a):
    
    if len(a)==2:
        return "YES"
        
    counts=Counter(a)
    keys = list(counts)
    if len(keys)==1:
        return "YES"
    elif len(keys) ==2:
        if abs(counts[keys[0]]-counts[keys[1]])<=1:
            return "YES"
            
    return "NO"        
          
    
          
res=[]                
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    tans=process(n,a)
    res.append(tans)

for e in res:
    print(e)    