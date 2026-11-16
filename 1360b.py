

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,a):
    limit=(2**70)
    a.sort()
    ans=limit
    for i in range(1,n,1):
        v1=a[i]-a[i-1]
        ans=min(ans,v1)
        
    return ans    
        
        
res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    tans=process(n,a)
    res.append(tans)
    
for e in res:
    print(e)    