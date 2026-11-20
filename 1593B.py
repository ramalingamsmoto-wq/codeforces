


import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

# 00 25 50 75
def process(n):
    moves=0
    c=[]
    sl=list(str(n))
    
    l=len(sl)
    i=l-1
    while True:
        if sl[i]=='0' or sl[i]=='5':
            v=get(sl,i,sl[i],moves)
            c.append(v)
            
                        
            
            
        else:
            sl.pop(i)  
            moves=moves+1  
        
        i=i-1
        
    return min(c)    
        
    

res=[]
for _ in range(ii()):
    n=ii()
    t=process(n)
    res.append(t)
    
for e in res:
    print(e)    