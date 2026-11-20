import sys
import math

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n):
    if n<4:
        return -1
    rem=n%4
    if rem==0 or rem==2:
        min=n//6
        r=n%6
        if r==4:
            min=min+1
        max=n//4
        if min==0 and max!=0:
            ans=f"{max} {max}"
        elif max==0 and min!=0:
            ans=f"{min} {min}"
        else:
            ans=f"{min} {max}"    
        return ans    
    else:
        return -1    
    
    
    
res=[]
for _ in range(ii()):
    n=ii()
    t=process(n)
    res.append(t)
    
    
for e in res:
    print(e)        
            
        