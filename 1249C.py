import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

import math

def process(n):
    
    i=2
    limit=(10**9)+1
    mxv=math.isqrt(limit)+1
    a=[]
    b=[]
    
    x=-1
    y=-1
    z=-1
    
    while True:
        
        if i>mxv:
            break
        if n%i==0:
            q=n//i
            if q!= i:
                a.append(i)    
                b.append(q)
        i=i+1        
    
    l=len(a)    
    print(f"a {a} b {b}")
    for i in range(l):
        tup=getv(a[i],b[i],n)
        
        
        
                
                
                
    if x==-1 and y==-1 and z==-1:
        tup=("NO",)
        return tup
    else:
        tup=("YES",[x,y,z])      
        return tup      


res=[]        
        
for _ in range(ii()):
    n=ii()
    tans=process(n)
    res.append(tans)

for tup in res:
    print(tup[0])   
    if tup[0] == "YES":
        print(*tup[1])