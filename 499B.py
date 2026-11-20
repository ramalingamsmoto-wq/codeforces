


import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

n,m=mi()
d=dict()
for _ in range(m):
    a,b=ls()
    if len(a)>len(b):
        d[a]=b
    elif len(b)>=len(a):
        d[a]=a
c=ls()    
b=[]
for i in range(n):
    sw=c[i]
    tw=d[sw]
    b.append(tw)
    
print(*b)    
    