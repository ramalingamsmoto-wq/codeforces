

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,k,a):
    s=0
    cnt=0
    for i in range(n):
        if a[i]>=k:
            s=s+a[i]
        elif a[i]==0 and s>0:
            s=s-1
            cnt=cnt+1
    return cnt        
 
 
res=[] 
for _ in range(ii()):
    n,k=mi()
    a=li()
    t=process(n,k,a)
    res.append(t)
    
for e in res:
    print(e)    