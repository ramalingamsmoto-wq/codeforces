
from collections import Counter


def process(n,a):
    counts=Counter(a)
    tc=counts[2]
    oc=counts[1]
    tc=tc%2
    if tc==1:
        if oc<2:
            return "NO"
        else:
            oc=oc-2
                
    if oc%2==0:
        return "YES"
    else:
        return "NO"  
          
res=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    tans=process(n,a)
    res.append(tans)
for e in res:
    print(e)    