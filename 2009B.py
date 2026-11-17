import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

res=[]
for _ in range(ii()):
    n=ii()
    b=[]
    for _ in range(n):
        s=input()
        idx=s.find("#")
        b.append(idx+1)
    res.append(b)    
for list in res:
    rlist=list[::-1]
    print(*rlist)    