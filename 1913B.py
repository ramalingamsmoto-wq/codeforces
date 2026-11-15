
from collections import Counter

def process(s):
    il=[int(c) for c in s]
    counts = Counter(il)
    zc=counts[0]
    oc=counts[1]
    
    for sbit in il:
        if sbit ==1:
            if zc > 0:
                zc=zc-1
            else:    
                break    
                
        if sbit==0:
            if oc > 0:
                oc=oc-1
            else:
                break    
                
    return oc+zc
    



t=int(input())
res=[]
for _ in range(t):
    s=input()
    tans=process(s)
    res.append(tans)
for e in res:
    print(e)    