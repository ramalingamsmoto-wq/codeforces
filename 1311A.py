

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(a,b):
    if a<=b:
        delta=b-a
        if delta==0:
            return 0
        else:
            if delta%2!=0:
                return 1
            else:
                return 2
    else:
        delta=a-b
        if delta%2==0:
            return 1
        else:
            return 2   
                                 
res=[]
for _ in range(ii()):
    a,b=mi()
    t=process(a,b)
    res.append(t)
    
for e in res:
    print(e)    
    