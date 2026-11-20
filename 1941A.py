import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()  
               
from bisect import bisect_left, bisect_right

def process(n,m,k,b,c):
    ways=0
    b.sort()
    c.sort()
    for e in b:
        oem=k-e
        index=bisect_right(c,oem)
        ways=ways+index
    return ways
    
res=[]
for _ in range(ii()):
    n,m,k=mi()
    b=li()
    c=li()
    ways=process(n,m,k,b,c)
    res.append(ways)
    
for e in res:
    print(e)    