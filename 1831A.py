

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    mx=max(a)+1
    b=[0]*n
    for i in range(n):
        v1=mx-a[i]
        b[i]=v1
    res.append(b)  
    
for e in res:
    print(*e)      