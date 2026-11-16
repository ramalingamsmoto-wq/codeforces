

import math

res=[]

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    
    idx = a.index(min(a))
    a[idx]=a[idx]+1
    tans = math.prod(a)
    res.append(tans)
    
for e in res:
    print(e)    
    