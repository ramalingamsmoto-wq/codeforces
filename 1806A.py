import sys
import math

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(sx,sy,tx,ty):
    
    #match y value
    moves=ty-sy
    if moves < 0:
        return -1
    currx=sx+moves
    curry=sy+moves
    
    if tx <= currx:
        moves=moves+ (currx-tx)
        return moves
    else:
        return -1    
    
    

res=[]
for _ in range(ii()):
    a,b,c,d=mi()
    tans=process(a,b,c,d)
    res.append(tans)
    
for e in res:
    print(e)    