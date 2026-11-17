import sys
from collections import Counter


input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,a):
    counts=Counter(a)
    moves=0
    cs=counts[1]-counts[-1]

    if cs<0:
        while cs<0:
        
            counts[-1]=counts[-1] - 1
            counts[1]=counts[1]+ 1
        
            moves=moves+1
            cs=counts[1]-counts[-1]
        
    moc=counts[-1]
    if moc%2!=0:
        counts[-1] =counts[-1] -1
        counts[1]=counts[1]+1
        moves=moves+1
        
    return moves    
    

res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    t=process(n,a)
    res.append(t)
    
for e in res:
    print(e)    
    