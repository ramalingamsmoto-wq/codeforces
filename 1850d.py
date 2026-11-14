

from collections import Counter

def process(n,k,a):
    dp=[0]*(n+1)
    counts=Counter(a)
    
    
    kl=list(counts)    
    kl.sort()
    e0=kl[0]
    dp[0]=counts[e0]
    mx=dp[0]
    l=len(kl)
    for i in range(1,l,1):
        
        if kl[i]-kl[i-1]<=k:
            dp[i]=dp[i-1]+counts[kl[i]]
            
        else:
            dp[i] =counts[kl[i]]
        mx=max(mx,dp[i])    
               
    return n-mx    
    


t=int(input())
res=[]
for _ in range(t):
    
    n,k=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    tans=process(n,k,a)
    res.append(tans)
for e in res:
    print(e)    