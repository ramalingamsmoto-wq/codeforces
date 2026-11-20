

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

from collections import Counter

def process(n,b):
    mx=max(b)
    mx=mx+1
    counts=Counter(b)
    flag=[0]*(n)
    for item,count in counts.items():
        
        
        
    
    
    
    
    
res=[]
for _ in range(ii()):
    n=ii()
    b=li()
    tans=process(n,b)
    res.append(tans)

for list1 in res:
    print(*list1)    