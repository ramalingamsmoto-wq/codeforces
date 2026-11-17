

import sys

from itertools import pairwise
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n=ii()
s=si()

pl=(list(pairwise(s)))
counts=Counter(pl)
max_pair = counts.most_common(1)[0][0]
rs=max_pair[0]+max_pair[1]
print(rs)