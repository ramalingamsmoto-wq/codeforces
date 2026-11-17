import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

import math
res=[]

for _ in range(ii()):
    l,r=mi()
    a=l
    b=l+1
    c = math.lcm(a, b)
    if c>=l and c<=r:
        res.append((a,b))
    else:
        res.append((-1,-1)) 
           
for tup in res:
    print(f"{tup[0]} {tup[1]}")        
