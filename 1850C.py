import sys
from collections import Counter
import math



# --- Fast Input (Bytes for numbers, Auto-decoded str for text) ---
rb = sys.stdin.buffer.readline
ii = lambda: int(rb())                        # int (pure bytes)
mi = lambda: map(int, rb().split())           # map of ints (pure bytes)
li = lambda: list(map(int, rb().split()))     # list of ints (pure bytes)
si = lambda: rb().rstrip().decode()           # normal str (e.g., "abc")
ls = lambda: rb().decode().split()            # list of normal strs

# --- Fast Output (Accepts int, str, bytes, and lists seamlessly) ---
out = []
pr = lambda x: out.append(str(x))
pa = lambda a: out.append(' '.join(map(str, a)))
flush = lambda: sys.stdout.buffer.write(('\n'.join(out) + '\n').encode())



for _ in range(ii()):
    ans=""
    for i in range(8):
        line=si()
        c=line.strip(".")
        ans=ans+c
    pr(ans)   
     
flush()      