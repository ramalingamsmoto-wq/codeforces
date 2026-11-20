

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def getlevel(n):
    
    cnt=0
    while True:
        
        if n%2!=0:
            break
        n=n//2
        cnt=cnt+1
    return cnt    
        
            


def process(w,h,n):
    l1=getlevel(w)
    v1=(2**l1)
    l2=getlevel(h)
    v2=(2**l2)
    mv=v1*v2
    
    #print(f" mv {mv}")
    
    if mv>=n:
        return "YES"
        
    return "NO"    
    
    
    
    
    
            
    
            
            
    
    
res=[]
for _ in range(ii()):
    w,h,n=mi()
    t=process(w,h,n)
    res.append(t)
    
for e in res:
    print(e)    