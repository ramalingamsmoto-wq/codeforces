

import sys

from datetime import datetime

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

res=[]
for _ in range(ii()):
    time_24=input()
    dt_obj = datetime.strptime(time_24, "%H:%M")
    time_12 = dt_obj.strftime("%I:%M %p")
    res.append(time_12)

for e in res:
    print(e)    
    
    