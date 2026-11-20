

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,ts,x,a):
    cs=sum(a)
    
    if cs >ts:
        return "NO"
        
    delta=ts-cs
    if delta%x==0:
        return "YES"
    return "NO"    
    
    
res=[]
for _ in range(ii()):
    n,s,x=mi()
    a=li()
    t=process(n,s,x,a)
    res.append(t)
    
for e in res:
    print(e)    