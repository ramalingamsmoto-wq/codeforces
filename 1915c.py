import sys
import math

# --- Pure Bytes Input ---
rb = sys.stdin.buffer.readline
ii = lambda: int(rb())                        # Single integer
mi = lambda: map(int, rb().split())           # Multiple integers
li = lambda: list(map(int, rb().split()))     # List of integers
sb = lambda: rb().rstrip()                    # Raw bytes string (e.g., b'abc')
lb = lambda: rb().split()                     # List of raw bytes strings

# --- Pure Bytes Output ---
out = bytearray()
pr = lambda x: out.extend(b'%d\n' % x)        # Append single integer as bytes
ps = lambda b: out.extend(b + b'\n')          # Append raw bytes line
pa = lambda a: out.extend(b' '.join(b'%d' % x for x in a) + b'\n') # Append int list
flush = lambda: sys.stdout.buffer.write(out)  # Write raw bytes in one syscall



for _ in range(ii()):
    n=ii()
    a=li()
    s=sum(a)
    root = math.isqrt(s)
    if root*root == s:
        ps(b"YES")
    else:
        ps(b"NO")  
        
flush()