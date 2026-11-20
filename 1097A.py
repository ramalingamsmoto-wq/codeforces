

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


tc=si()
hc=ls()
hs={hc[0][1],hc[1][1],hc[2][1],hc[3][1],hc[4][1]}
hr={hc[0][0],hc[1][0],hc[2][0],hc[3][0],hc[4][0]}

if tc[0] in hr or tc[1] in hs:
    print("YES")
else:
    print("NO")