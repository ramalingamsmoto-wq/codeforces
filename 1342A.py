

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(x,y,a,b):
    
    v1=0
    v2=0
    v3=0
    if (x>0 and y>0) or (x<0 and y<0):
        mx=max(x,y)
        mn=min(x,y)
        
        delta=abs(mx-mn)
        v1=v1+(delta*a)
        v1=v1+(mn*b)
        
        v2=abs(x*a)+abs(y*a) 
        ans=min(v1,v2)
        return ans
    else:
        v3=abs(x*a)+abs(y*a)  
        return v3
        
     
        
        
        
res=[]
for _ in range(ii()):
    x,y=mi()
    a,b=mi()
    t=process(x,y,a,b)
    res.append(t)
    
for e in res:
    print(e)    
    
    