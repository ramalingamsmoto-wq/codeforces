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

for _ in range(ii()):
    n,x=mi()
    dp=[0]*1001
    dp[1]=2
    if n <=2:
        pr(1)
    else:    
        i=2
        while True:
            v1=dp[i-1]+x
            dp[i]=v1
            if v1>=n:
                break
            i=i+1    
        pr(i)
    
flush()    
    
    
    
    
    