import sys
from collections import Counter 

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,m,a):
    counts=Counter(a)
    counts = Counter({ch: counts[ch] for ch in "ABCDEFG"})

    #print(f"counts {counts}")
    pn=0
    for item,count in counts.items():
        if count<m:
            pn=pn+m-count
            
    return pn        
    
    
res=[]
for _ in range(ii()):
    n,m=mi()
    a=si()
    t=process(n,m,a)
    res.append(t)

for e in res:
    print(e)    