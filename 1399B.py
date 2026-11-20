

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,c,o):
    
    mnc=min(c)
    mno=min(o)
    moves=0
    for i in range(n):
        if c[i] > mnc and o[i] > mno:
            cm=c[i]-mnc
            om=o[i]-mno
            common=min(cm,om)
            moves=moves+common+(cm-common)+(om-common)
        elif c[i]> mnc:
            cm=c[i]-mnc
            moves=moves+cm
        elif o[i] > mno:
            om=o[i]-mno
            moves=moves+om
    return moves        
        
res=[]
for _ in range(ii()):
    n=ii()
    c=li()
    o=li()
    moves=process(n,c,o)
    res.append(moves)
    
for e in res:
    print(e)    