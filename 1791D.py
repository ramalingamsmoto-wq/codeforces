import sys
from collections import Counter
import math


# --- Pure Bytes Input ---
rb = sys.stdin.buffer.readline
ii = lambda: int(rb())                        # Single integer
mi = lambda: map(int, rb().split())           # Multiple integers
li = lambda: list(map(int, rb().split()))     # List of integers
sb = lambda: rb().rstrip()                    # Raw bytes string (e.g., b'abc')
lb = lambda: rb().split()                     # List of raw bytes strings
ms = lambda: map(str, rb().split()) 

# --- Pure Bytes Output ---
out = bytearray()
pr = lambda x: out.extend(b'%d\n' % x)        # Append single integer as bytes
ps = lambda b: out.extend(b + b'\n')          # Append raw bytes line
pa = lambda a: out.extend(b' '.join(b'%d' % x for x in a) + b'\n') # Append int list
flush = lambda: sys.stdout.buffer.write(out)  # Write raw bytes in one syscall

def process(n,s):
    pre=[0]*n
    suf=[0]*n
    
    hs=set()
    for i in range(n):
        hs.add(s[i])
        l=len(hs)
        pre[i]=l
        
    hs=set()    
    for i in range(n-1,-1,-1):
        hs.add(s[i])
        l=len(hs)
        suf[i]=l
        
    mx=-1
    for i in range(0,n-1,1):
        v1=pre[i]+suf[i+1] 
        mx=max(mx,v1) 
        
    return mx    
            
        

for _ in range(ii()):
    n=ii()
    s=sb()
    tans=process(n,s)
    pr(tans)
    
flush()    