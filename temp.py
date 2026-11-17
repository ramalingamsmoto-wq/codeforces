import sys

from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



        
        
        
import math
from itertools import pairwise

list1=[]
for i in range(3,900,1):
    a=14
    b=21
    c = math.lcm(a, b)
    list1.append(c)
    
    print(f"a {a} b {b} lcm {c}")
    


v1=is_strictly_increasing = all(a < b for a, b in pairwise(list1))
print(f"v1 {v1}")


