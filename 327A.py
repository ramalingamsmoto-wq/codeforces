


import sys

from collections import Counter 

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n=ii()
a=li()


def update(a,counts):
    dc=counts.copy()
    for e in a:
        if e==1:
            dc[0]=dc[0]+1
            dc[1]=dc[1]-1
        else:
            dc[0]=dc[0]-1
            dc[1]=dc[1]+1  
            
    return dc[1]        
    
mx=-1
counts=Counter(a)
for i in range(n):
    for j in range(i + 1, n + 1):
        v1=update(a[i:j],counts)
        mx=max(mx,v1)

print(mx)        